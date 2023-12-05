from .connection_sql import OpenDB
from flask import current_app as app
from flask import jsonify, request
from sc.runner import insert_ticks, insert_investors_data,insert_metadata
import json


from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required, create_access_token


from .models import User, TokenBlocklist
from . import db, jwt
from datetime import datetime, timedelta,timezone

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


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    pwd = request.json.get("pwd", None)
    user = User.query.filter_by(username=username).first()
    if user:
        if user.check_password(pwd):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", None)
    pwd = request.json.get("pwd", None)
    email = request.json.get("email", None)
    print(email)
    user = User.query.filter_by(username=username).first()
    print(user)
    if user:
        return jsonify({"msg": "Bad username or password"}), 401
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, username=username, pwd=User.set_password(pwd))
    print(new_user)
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "Registerred"}), 200


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
'''
# Callback function to check if a JWT exists in the redis blocklist
@app.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None
'''

# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None

# Endpoint for revoking the current users access token. Saved the unique
# identifier (jti) for the JWT into our database.
@app.route("/logout", methods=["DELETE"])
@jwt_required()
def modify_token():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify(msg="JWT revoked")