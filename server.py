from bottle import (
    Bottle, jinja2_view, run,
    abort, static_file, request,
)

from functools import partial
import importlib
import judger
from pathlib import Path
import re
import sqlite3

app = Bottle()
jinja2_template = partial(jinja2_view, template_lookup=['templates'])


def parse_question_folder():
    """Parse all questions under questions/ and return file mapping."""
    q_pths = Path('questions').glob('q_*.py')
    extract_q_name = re.compile('^q_(.+)$').match
    return {
        extract_q_name(pth.stem).group(1): pth
        for pth in q_pths
    }


@app.route('/', method='GET')
@jinja2_template('index.html')
def index(msg=''):
    return {'msg': msg}


@app.route('/question/', method='GET')
@jinja2_template('questions.html')
def list_question():
    all_questions = parse_question_folder()
    return {
        'questions': all_questions.keys()
    }


def read_question(q_name):
    q_pth = parse_question_folder()[q_name]
    doc_string = []
    answer_example = []
    with q_pth.open() as f:
        # read doc string
        for line in f:
            if line.strip() in ["'''", '"""']:
                break
            doc_string.append(line)

        # read answer example
        reading_ans = False
        for line in f:
            if line.startswith('def answer('):
                reading_ans = True
            if not reading_ans:
                continue
            answer_example.append(line)
            if line.startswith('    return '):
                break
    doc_string[0] = doc_string[0][len("'''"):]
    q_name, q_desc = doc_string[0][len('Question '):].split(': ', 1)
    doc_string = doc_string[2:]
    return q_name, q_desc, ''.join(doc_string), ''.join(answer_example)


_db_name = 'codegame.db'
_db_backup = 'codegame.prv.db'
#create default table
_create_db_tables_sql = '''\
CREATE TABLE GAME (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT,
    question TEXT,
    timestamp DATETIME DEFAULT NULL
);

CREATE TABLE RESULT (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT,
    submit TEXT,
    codingtime TEXT,
    timestamp DATETIME DEFAULT NULL,
    judge TEXT,
    gameid INTEGER,
    FOREIGN KEY(gameid) REFERENCES GAME(id)
);
'''


@app.route('/admin/', method='POST')
def reload_db():
    # if database does not exist, create a new one without renaming.
    # otherwise move the original databse as xxx.prev
    try:
        Path(_db_name).rename(_db_backup)
        db_existed = True
    except OSError as e:
        db_existed = False
    # recreate the database. If any move fails, move back the original databse.
    try:
        conn = sqlite3.connect(_db_name)
        conn.executescript(_create_db_tables_sql)
        conn.commit()
    except Exception as e:
        conn.close()
        if db_existed:
            Path(_db_name).unlink()
            Path(_db_backup).rename(_db_name)
        return False
    else:
        if db_existed:
            Path(_db_backup).unlink()
        return True


# @app.route('/teacher/', method='POST')
# def teacher():
#     redirect('/teacher/{}/'.format(request.forms.get('teacherName')))


def connect_db():
    conn = sqlite3.connect(_db_name)
    conn.row_factory = sqlite3.Row
    return conn


def get_games():
    games = []
    with connect_db() as conn:
        records = conn.execute(
            'SELECT * FROM GAME ORDER BY timestamp DESC'
        ).fetchall()
        try:
            for record in records:
                games.append(
                    {'id': record['id'],
                     'name': record['name'],
                     'question': record['question'],
                     's_time': record['timestamp']})

        except:
            pass
    return games

_insert_game_sql = 'INSERT INTO GAME (name, question, timestamp) VALUES %s '


def insert_games(games=[]):
    with connect_db() as conn:
        for game in games:
            vals = ','.join(['("%s", "%s", date(\'now\') )' % (item['name'], item['question'] ) for item in games])
        try:
            conn.execute(_insert_game_sql % vals)
            conn.commit()
        except:
            return False
    return True

_get_result_sql = 'SELECT * FROM RESULT'
_get_result_id_sql = ' WHERE RESULT.gameid = %s ORDER BY RESULT.name ASC'


def get_results(gameid=''):
    #list all game result
    results = []
    with connect_db() as conn:
        if not gameid:
            records = conn.execute(_get_result_sql).fetchall()
        else:
            records = conn.execute(_get_result_sql + _get_result_id_sql % gameid)
        try:
            for record in records:
                results.append(
                    {'id': record['id'],
                     'name': record['name'],
                     'submit': record['submit'],
                     'codingtime': record['codingtime'],
                     'timestamp': record['timestamp'],
                     'judge': record['judge'],
                     'gameid': record['gameid']})
        except Exception:
            pass
    return results

_ins_result_sql = 'INSERT INTO RESULT (name, submit, codingtime, timestamp, judge, gameid) VALUES '


#insert result each by each
def insert_result(**argd):
    with connect_db() as conn:
        try:
            isql = _ins_result_sql + "(?, ?, ?, date('now'), ?, ?)"
            conn.execute(
                isql,
                (argd['name'],
                argd['submit'],
                argd['codingtime'],
                argd['judge'],
                argd['gameid'])
            )
            conn.commit()
        except Exception as e:
            print(e)
            return False
    return True


@app.route('/test-submit/<question_name>/', method='GET')
def submit(question_name='foo'):
    q_pth = 'questions/q_%s.py' % question_name
    ans_text = ''
    importlib.reload(judger)
    tp, test_output = judger.run_judge(q_pth, ans_text)
    return test_output


@app.route('/play/', method='GET')
@jinja2_template('play.html')
def play():
    game = get_games()[-1]
    q_name, q_desc, q_doc, q_ex_ans = read_question(game['name'])
    return {
        'q_name': q_name,
        'q_desc': q_desc,
        'q_doc': q_doc,
        'example_ans': q_ex_ans
    }


@app.route('/play/', method='POST')
@jinja2_template('play.html')
def submit_play():
    game = get_games()[-1]
    q_name, q_desc, q_doc, q_ex_ans = read_question(game['name'])
    player_name = request.forms.get('player_name')
    answer_text = request.forms.get('code')

    q_pth = 'questions/q_%s.py' % q_name
    importlib.reload(judger)
    test_prog, test_output = judger.run_judge(q_pth, answer_text)

    # insert result into db
    insert_result(
        name=player_name,
        submit=answer_text,
        codingtime="60",
        judge=str(test_prog.success),
        gameid=str(game['id'])
    )

    history = ''
    return {
        'q_name': q_name,
        'q_desc': q_desc,
        'q_doc': q_doc,
        'example_ans': answer_text,
        'player_name': player_name,
        'result': test_output,
        'history': history
    }


@app.route('/judge/', method='GET')
@jinja2_template('judge.html')
def judge():
    return {'msg': 'judge'}


@app.route('/gameadmin/', method='GET')
@jinja2_template('admin.html')
def admin(msg='welcome'):
    r_form = '''\
            <form action="/gameadmin/" method="post" id="adminform">
            CreateGame: <input name="gamename" type="text" />
            <input name="operation" id="operation" value="" type="hidden" />
            <input name="create" value="Create" type="button" onClick="Create()"/>
            <input name="random" value="Random" type="button" onClick="Random()"/>
            </form>
    '''
    r_js_form = '''
    function Create(e) {
        document.getElementById("operation").value = "Create";
        console.log(document.getElementById("operation").value);
        document.getElementById("adminform").submit();
        return false;
    }
    function Random(e) {
        document.getElementById("operation").value = "Random";
        console.log(document.getElementById("operation").value);
        document.getElementById("adminform").submit();
        return false;
    }
    '''
    return {'msg':msg,
            'form': r_form,
            'js':r_js_form}


import random

@app.route('/gameadmin/', method='POST')
@jinja2_template('admin.html')
def doAdmin():
    operation = request.forms.get('operation','Random').lower()
    print('%s' % request.forms.get('operation',''))
    msg = []
    print(list_question())
    if operation == 'create':
        #create new game
        qname = request.forms.get('gamename','')
        if qname and qname in parse_question_folder().keys():
            if not insert_games( [ {'name':qname, 'question':'empty'},]):
                msg.append('Error: Cannot Create Game! %s' % qname)
            else:
                msg.append('SUCCESS Create Game! %s' % qname)
    else:
        #random generate game
        keys = list(parse_question_folder().keys())
        qname = random.choice(  keys )
        if not insert_games( [ {'name':qname, 'question':'empty'},]):
            msg.append('Error: Cannot Create Game! %s' % qname)
        else:
            msg.append('SUCCESS Create Game! %s' % qname)
    return admin(msg=';'.join(msg))

@app.route('/test/', method='GET')
@jinja2_template('admin.html')
def testdb():
    reload_db()
    msg = []
    if not insert_games([{'name': 'foo', 'question': 'NO USE'}]):
        msg.append('insert db failed')
    games = get_games()
    if not games:
        msg.append('there is no game in db')
    if not insert_result(name='test_foo', submit='test_bar', codingtime='57', judge='Pass', gameid='0'):
        msg.append('Add result failed')
    record = get_results()
    if not record:
        msg.append('Get result failed')
    if not msg:
        msg.append('All Test Success!')
    return {'msg': ';'.join(msg)}


@app.route('/static/<path:path>')
def get_static_file(path):
    return static_file(path, './static')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
