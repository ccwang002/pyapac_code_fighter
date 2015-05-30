from bottle import Bottle, jinja2_view, run, abort, static_file, request

app = Bottle()

@app.route('/')
def landing_page():
    return 'Welcome to Code Fighter!'
