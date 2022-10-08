from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   unique=True,
                   nullable=False)
    email = db.Column(db.String(56), unique=True)
    password = db.Column(db.String(126), nullable=False)
    notes = db.relationship('Note', backref='note')

    def __repr__(self):
        return f'User: {self.email}'


class Note(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   unique=True,
                   nullable=False)
    text = db.Column(db.String(124), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.text}'