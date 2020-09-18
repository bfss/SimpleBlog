from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    introduce = db.Column(db.String(120), nullable=True)

    post = db.relationship('Post',backref='author',lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('不可读的值')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(48),nullable = False)
    body = db.Column(db.Text, nullable = False)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow())
    is_deleted = db.Column(db.Boolean(), nullable = False, default=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))