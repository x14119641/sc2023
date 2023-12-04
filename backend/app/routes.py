from .connection_sql import OpenDB
from flask import current_app as app
from flask import jsonify, request
from sc.runner import insert_ticks, insert_investors_data,insert_metadata
import json
from flask_login import LoginManager, AnonymousUserMixin,current_user

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


_PATH_DB_ = 'sc/db.db'


def make_dicts(cursor,rows):
    cols = [item[0] for item in cursor.description]
    data= []

    for i,row in enumerate(rows):
        data.append({cols[i]:row[i]})
    return data



@app.route('/api/tickers', methods=['GET'])
def tickers():
    sql= '''
            SELECT t.tick , t.name, m.sector, m.industry, m.country
            FROM tickers t
            INNER JOIN metadata m 
            ON t.tick = m.tick ;
        '''
    with OpenDB(_PATH_DB_) as conn:
        cur = conn.execute(sql)
        data=cur.fetchall()
    return jsonify(data)



@app.route('/api/institutional/<tick>', methods=['GET'])
def tickerInstitutional(tick):
    sql= f'''
            SELECT ih.* FROM institutional_holdings ih  
            WHERE ih.tick = '{tick.upper()}'
            ORDER BY ih.refreshed_page_date DESC;
        '''
    with OpenDB(_PATH_DB_) as conn:
        cur = conn.execute(sql)
        data=cur.fetchall()
    # print(data)
    return jsonify(data)

@app.route('/api/metadata/tickers', methods=['GET'])
def tickersMeta():
    sql= '''
            SELECT s.tick,s.last_sale, s.net_change, s.change_perc, s.market_cap, s.ipo_year, s.inserted  FROM (
                SELECT t.*,
                    ROW_NUMBER() OVER(PARTITION BY t.tick ORDER BY t.inserted DESC) as rnk
                FROM metadata t) s
            WHERE s.rnk = 1;
        '''
    with OpenDB(_PATH_DB_) as conn:
        cur = conn.execute(sql)
        data=cur.fetchall()
    return jsonify(data)



@app.route('/api/insert_tickers', methods=['GET'])
def insert_tickers():
    # data = insert_ticks()
    data='doing insert'
    return jsonify(data)


@app.route('/api/insert_institutional', methods=['POST'])
def insert_institutional():
    refreshed_date = json.loads(request.data.decode())['refreshed_date']
    print(refreshed_date)
    # data = insert_investors_data(refreshed_date or '')
    data='doing insert'
    return jsonify(data)

@app.route('/api/insert_metadata', methods=['Get'])
def insert_metadata():
    # data = insert_metadata(refreshed_date or '')
    data='doing insert'
    return jsonify(data)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"