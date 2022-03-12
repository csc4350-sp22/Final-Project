from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)


# create Comment database


class Rating(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    comment = db.Column(db.String(300), unique=False, nullable=False)
    movie_id = db.Column(db.Integer, unique=False, nullable=False)


db.create_all()
