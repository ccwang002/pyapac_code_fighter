from bottle import Bottle, jinja2_view, run, abort, static_file, request

app = Bottle()

@app.route('/')
def landing_page():
    return 'Welcome to Code Fighter!'

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
