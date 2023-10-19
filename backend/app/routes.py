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


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"