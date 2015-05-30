from bottle import Bottle, jinja2_view, run, abort, static_file, request
from functools import partial
from pathlib import Path
import re

app = Bottle()
jinja2_template = partial(jinja2_view, template_lookup=['templates'])


@app.route('/', method='GET')
@jinja2_template('index.html')
def index(msg=''):
    return {'msg': 'abc'}


@app.route('/question/', method='GET')
@jinja2_template('questions.html')
def list_question():
    questions = Path('questions').glob('q_*.py')
    extract_q_name = re.compile('^q_(.+)$').match

    return {
        'questions': [extract_q_name(p.name).group(1) for p in questions]
    }

@app.route('/play/', method='POST')
@jinja2_template('play.html')
def play():






if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
