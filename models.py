import hashlib
from datetime import datetime
from sqlalchemy import exc

import errors
from app import db


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    @classmethod
    def by_id_user(cls, obj_id, user_id):
        obj = cls.query.filter_by(id=obj_id).filter(cls.user_id==user_id).all()
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck


class Users(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='users')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password: str):
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "email": self.email
        }


class Post(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return '<Post {}>'.format(self.title)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            "content": self.content,
            "created_at": self.created_at,
            "user_id": self.user_id,
                }
