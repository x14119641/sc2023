from app import db
import bcrypt 


roles_users = db.Table('roles_users',
    db.Column('id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True) # Hash pwd representation

    roles = db.relationship('Role', secondary=roles_users, backref='role')
 
    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def set_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), 
                                           bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.pwd)




# create table in database for storing roles
class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)