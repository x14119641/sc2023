from flask import current_app as app
from flask import jsonify, request


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"