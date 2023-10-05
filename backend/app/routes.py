from flask import current_app as app
from flask import jsonify, request


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"