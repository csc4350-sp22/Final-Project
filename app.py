# pylint: disable = missing-module-docstring
# pylint: disable = missing-class-docstring

# pylint: disable = plyint(no-member)


import os
import random
import flask
from flask import session
from flask_sqlalchemy import SQLAlchemy
from wiki import wiki_search
from tmdb import movie_search


app = flask.Flask(__name__)


app.secret_key = "ABC"


# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create User database


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)


# create Comment database


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    comment = db.Column(db.String(300), unique=False, nullable=False)
    movie = db.Column(db.Integer, unique=False, nullable=False)


db.create_all()


@app.route('/index', methods=['GET', 'POST'])
# pylint: disable = missing-function-docstring
def index():

    if flask.request.method == "POST":

        if session.get("user"):
            username = session["user"]

        data = flask.request.form
        rating = data["rating"]
        comment = data["comment"]
        movie = data["movie"]

        new_comment = Comment(
            rating=rating, comment=comment, movie=movie, username=username)

        print(rating)
        print(comment)
        print(movie)
        print(username)

        db.session.add(new_comment)
        db.session.commit()
        flask.redirect(flask.url_for("index"))

    movies_list = [70981, 299534, 634649, 207703, 566525]

    random_mov = random.choice(movies_list)

    movie_info = movie_search(random_mov)

    wiki = wiki_search(movie_info['title'])

    reviews = Comment.query.filter_by(movie=random_mov).all()

    return flask.render_template(
        "index.html",
        movie_info=movie_info,
        movie=random_mov,
        wiki=wiki,
        reviews=reviews,

    )


@app.route('/', methods=['GET', 'POST'])
def login():
    if flask.request.method == "POST":

        username = flask.request.form.get("username")

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            session["user"] = username
            return flask.redirect(flask.url_for("index"))

        else:
            flask.flash("Invalid Username!")

    return flask.render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == "POST":

        username = flask.request.form.get("username")

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            flask.flash("Username already exists!")
            return flask.redirect(flask.url_for("register"))

        else:
            # make new user
            new_user = User(username=username)
            # add new user
            db.session.add(new_user)
            # commit session
            db.session.commit()
            # redirect to login page
            return flask.redirect(flask.url_for("login"))

    return flask.render_template("register.html")


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=os.getenv("PORT", "8080"),
    debug=True
)
