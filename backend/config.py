import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = 'dq9nt3lkng8*-12dasa12amc'
    # SECRET_KEY = 'x654dqw56q5we4/89asd6xd49'
    # JWT_ACCESS_TOKEN_EXPIRES = Default: datetime.timedelta(minutes=15)
    # JWT_AUTH_SECURE = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    # REST_USE_JWT = True
    # REST_SESSION_LOGIN = False
    # ALPHA_KEY = 'QXZT2OVO02A3MWQB'