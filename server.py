from bottle import (
    Bottle, jinja2_view, run,
    static_file, request
)
from collections import OrderedDict
from datetime import datetime
from functools import partial
import importlib
from itertools import groupby
import judge
import operator
from pathlib import Path
import random
import re
import sqlite3

app = application = Bottle()
jinja2_template = partial(jinja2_view, template_lookup=['templates'])


_db_name = '/tmp/codegame.db'
_db_backup = '/tmp/codegame.prv.db'

# default table schema
_create_db_tables_sql = '''\
CREATE TABLE game (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT,
    question TEXT,
    timestamp DATETIME DEFAULT NULL
);

CREATE TABLE result (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT,
    submit TEXT,
    codingtime TEXT,
    timestamp DATETIME DEFAULT NULL,
    judge TEXT,
    gameid INTEGER,
    FOREIGN KEY(gameid) REFERENCES game(id)
);
'''


def connect_db():
    conn = sqlite3.connect(_db_name)
    conn.row_factory = sqlite3.Row
    return conn


def get_games(limit=-1):
    sql_latest_games = 'SELECT * FROM game ORDER BY timestamp DESC'
    games = []
    with connect_db() as conn:
        if limit < 0:
            records = conn.execute(sql_latest_games).fetchall()
        else:
            records = conn.execute(
                sql_latest_games + ' LIMIT ?', str(limit)
            ).fetchall()
    for record in records:
        games.append({
            'id': record['id'],
            'name': record['name'],
            'question': record['question'],
            's_time': record['timestamp']
        })
    return games


def insert_games(games):
    try:
        conn = connect_db()
        conn.executemany(
            'INSERT INTO game(name, question, timestamp) '
            'VALUES (?, ?, datetime("now"))',
            map(operator.itemgetter('name', 'question'), games)
        )
        conn.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True


def get_results(gameid=''):
    _get_result_sql = 'SELECT * FROM result'
    _get_result_id_sql = ' WHERE result.gameid = %s ORDER BY result.name ASC'
    #  list all game result
    results = []
    with connect_db() as conn:
        if not gameid:
            records = conn.execute(_get_result_sql).fetchall()
        else:
            sql_cmd = _get_result_sql + _get_result_id_sql % gameid
            records = conn.execute(sql_cmd).fetchall()
        try:
            # for record in records:
            #     results.append({
            #         'id': record['id'],
            #         'name': record['name'],
            #         'submit': record['submit'],
            #         'codingtime': record['codingtime'],
            #         'timestamp': record['timestamp'],
            #         'judge': record['judge'],
            #         'gameid': record['gameid']
            #     })
            results = [dict(rec) for rec in records]
        except Exception as e:
            print(e)
    return results

# insert result each by each
def insert_result(name, submit, codingtime, judge, gameid):
    sql_cmd = (
        'INSERT INTO '
        'result(name, submit, codingtime, timestamp, judge, gameid) '
        "VALUES (?, ?, ?, datetime('now'), ?, ?)"
    )
    with connect_db() as conn:
        try:
            conn.execute(sql_cmd, (name, submit, codingtime, judge, gameid))
            conn.commit()
        except Exception as e:
            print(e)
            return False
    return True


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


@app.route('/admin/', method='POST')
def reload_db():
    # if database does not exist, create a new one without renaming.
    # otherwise move the original databse as xxx.prev
    try:
        Path(_db_name).rename(_db_backup)
        db_existed = True
    except OSError:
        db_existed = False
    # recreate the database. If any move fails, move back the original databse.
    try:
        conn = sqlite3.connect(_db_name)
        conn.executescript(_create_db_tables_sql)
        conn.commit()
    except Exception:
        # roll back using old database
        conn.close()
        if db_existed:
            Path(_db_name).unlink()
            Path(_db_backup).rename(_db_name)
        return False
    else:
        conn.close()
        if db_existed:
            Path(_db_backup).unlink()
        return True


@app.route('/play/', method='GET')
@jinja2_template('play.html')
def play():
    game = get_games(limit=1)[-1]
    q_pth = parse_question_folder()[game['name']]
    q_name, q_desc, q_doc, q_ex_ans = judge.read_question(q_pth)
    return {
        'q_name': q_name,
        'q_desc': q_desc,
        'q_doc': q_doc,
        'example_ans': q_ex_ans
    }


@app.route('/play/', method='POST')
@jinja2_template('play.html')
def submit_play():
    game = get_games(limit=1)[-1]
    q_pth = parse_question_folder()[game['name']]
    q_name, q_desc, q_doc, q_ex_ans = judge.read_question(q_pth)
    player_name = request.forms.get('player_name')
    answer_text = request.forms.get('code')

    importlib.reload(judge)
    test_prog, test_output = judge.run_judge(q_pth, answer_text)

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
def judge_status():
    def parse_time_stamp(r):
        r['timestamp'] = (now - datetime.strptime(
            r['timestamp'],
            "%Y-%m-%d %H:%M:%S"
        )).total_seconds()
        return r['timestamp']

    latest_game = get_games(limit=1)[0]
    results = get_results(latest_game['id'])
    now = datetime.utcnow()
    submit_by_names = OrderedDict([
        (k, sorted(v, key=parse_time_stamp, reverse=True))
        for k, v in groupby(results, lambda r: r['name'])
    ])

    # find latest submit time
    latest_success_submit = OrderedDict.fromkeys(submit_by_names.keys())
    for name, submit_history_time_asc in submit_by_names.items():
        last_success_time = None
        for submit in submit_history_time_asc:
            if submit['judge'] == 'True':
                last_success_time = submit['timestamp']
        latest_success_submit[name] = last_success_time

    # game info
    q_pth = parse_question_folder()[latest_game['name']]
    q_name, q_desc, q_doc, q_ex_ans = judge.read_question(q_pth)

    return {
        'q_name': q_name,
        'q_desc': q_desc,
        'q_doc': '\n'.join(q_doc.splitlines()[3:13] + ['... (stripped)']),
        'results': submit_by_names,
        'latest_success': latest_success_submit
    }


@app.route('/gameadmin/', method='GET')
@jinja2_template('admin.html')
def admin(msg=None):
    all_questions = parse_question_folder()
    return {
        'msg': msg,
        'questions': all_questions.keys(),
    }


@app.route('/gameadmin/', method='POST')
@jinja2_template('admin.html')
def doAdmin():
    operation = request.forms.get('operation', 'Random').lower()
    print('%s' % request.forms.get('operation', ''))
    msg = []
    if operation == 'create':
        # create new game
        qname = request.forms.get('gamename', '')
        if qname and qname in parse_question_folder().keys():
            if not insert_games([{'name': qname, 'question': 'empty'}]):
                msg.append(
                    'Error: Cannot create game: <code>%s</code>' %
                    qname)
            else:
                msg.append('Success: Create game: <code>%s</code>' % qname)
    else:
        # random generate game
        keys = list(parse_question_folder().keys())
        qname = random.choice(keys)
        if not insert_games([{'name': qname, 'question': 'empty'}]):
            msg.append('Error: Cannot create game <code>%s</code>' % qname)
        else:
            msg.append('Success: Create game <code>%s</code>' % qname)
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
    ret_val = insert_result(
        name='test_foo', submit='test_bar',
        codingtime='57', judge='Pass', gameid='0'
    )
    if not ret_val:
        msg.append('Add result failed')
    record = get_results()
    if not record:
        msg.append('Get result failed')
    if not msg:
        msg.append('All Test Success!')
    return {'msg': '; '.join(msg)}


@app.route('/static/<path:path>')
def get_static_file(path):
    return static_file(path, './static')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
