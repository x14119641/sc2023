from .connection_sql import OpenDB
from flask import current_app as app
from flask import jsonify, request




_PATH_DB_ = 'small_scarper/db.db'


def make_dicts(cursor,rows):
    cols = [item[0] for item in cursor.description]
    data= []

    for i,row in enumerate(rows):
        data.append({cols[i]:row[i]})
    return data



@app.route('/api/tickers', methods=['GET'])
def tickers():
    with OpenDB(_PATH_DB_) as conn:
        cur = conn.execute('SELECT * FROM tickers')
        # print(cur.description)
        data=cur.fetchall()
        # print(len(data))
    return jsonify(data)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"