from app import app, db
import random
import os

import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User, Rating
from wiki import wiki_search
from tmdb import movie_search


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


# pylint: disable = missing-function-docstring
@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login_post():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("home"))

    else:
        flask.flash("Invalid Username!")
        return flask.redirect(flask.url_for("login"))


@app.route("/register")
def signup():
    return flask.render_template("register.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        flask.flash("Username already exists!")
        return flask.redirect(flask.url_for("register"))
    else:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/rate", methods=["POST"])
def rate():
    data = flask.request.form
    rating = data.get("rating")
    comment = data.get("comment")
    movie_id = data.get("movie_id")

    new_rating = Rating(
        username=current_user.username,
        rating=rating,
        comment=comment,
        movie_id=movie_id,
    )

    db.session.add(new_rating)
    db.session.commit()
    return flask.redirect("home")


@app.route("/")
def landing():
    if current_user.is_authenticated:
        return flask.redirect("home")
    return flask.redirect("login")


@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect("login")


@app.route("/home", methods=["GET", "POST"])
# pylint: disable = missing-function-docstring
def home():

    MOVIE_IDS = [70981, 299534, 634649, 207703, 566525]

    movie_id = random.choice(MOVIE_IDS)

    movie_info = movie_search(movie_id)

    wiki = wiki_search(movie_info["title"])

    reviews = Rating.query.filter_by(movie_id=movie_id).all()

    return flask.render_template(
        "home.html",
        movie_info=movie_info,
        movie_id=movie_id,
        wiki=wiki,
        reviews=reviews,
    )


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page


@bp.route("/milestone3")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


app.register_blueprint(bp)


@app.route("/movie_comments", methods=["GET", "POST"])
def movie_comments():

    output = Rating.query.filter_by(username=current_user.username).all()
    nums_output = len(output)
    a = []

    for i in range(nums_output):
        a.append(
            {
                "id": output[i].id,
                "movie_id": output[i].movie_id,
                "rating": output[i].rating,
                "comment": output[i].comment,
                "username": output[i].username,
            }
        )
    return flask.jsonify(a)


@app.route("/delete_reviews", methods=["POST"])
def delete_reviews():

    reviews = list(flask.request.get_json(force=True))

    if len(reviews) == 0:
        return flask.jsonify({"SUCCESS": "FALSE"})

    for review in reviews:
        Rating.query.filter_by(id=review["id"]).delete()
        db.session.commit()

    return flask.jsonify({"SUCCESS": "TRUE"})


@app.route("/edit_reviews", methods=["POST"])
def edit_reviews():

    reviews = list(flask.request.get_json(force=True))
    if len(reviews) == 0:
        return flask.jsonify({"SUCCESS": "FALSE"})

    for review in reviews:

        Rating.query.filter_by(id=review["id"]).update(
            {"comment": review["comment"], "rating": review["rating"]},
        )
        db.session.commit()

    return flask.jsonify({"SUCCESS": "TRUE"})


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
