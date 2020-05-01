from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from . import login_manager
from datetime import datetime

# @login_manager.user_loader

# def user_load(user_id):
#     return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    # pitch = db.relationship('1, 2 and .. GO!', backref= author, lazy = 'dynamic')
    # comments = db.relationship('Say Something', backref=author, lazy= 'dynamic')

    def __repr__(self):
        return f'Author {self.author}'
