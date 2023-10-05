from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Libraries
cors = CORS(
    # origins=["http://localhost:8080","http://localhost:5000", 
    #          "http://10.0.14.245:8080", "http://127.0.0.1:5000", "http://127.0.0.1:8080",
    #          "https://query1.finance.yahoo.com"], 
    headers=['Content-Type'], 
    expose_headers=['Access-Control-Allow-Origin'], 
    supports_credentials=True)
db = SQLAlchemy(
    #session_options={'autocommit': True}
    )
# migrate = Migrate()
# jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        # migrate.init_app(app, db)
        # jwt.init_app(app)
        cors.init_app(
            app,
            # origins=["http://localhost:8080","http://localhost:5000", "http://zitroapi.pre.landbased.zitro.lan/es/login/", "http://10.0.14.245:8080/"], 
            headers=['Content-Type'], 
            expose_headers=['Access-Control-Allow-Origin'], 
            supports_credentials=True
        )
        from . import routes, models

        return app