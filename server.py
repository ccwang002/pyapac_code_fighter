from bottle import Bottle, jinja2_view, run, abort, static_file, request

app = Bottle()

@app.route('/', method='GET')
@jinja2_view('index.html', template_lookup=['templates'])
def index(msg=''):
    return {'msg': msg}

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
