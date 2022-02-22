#pylint: disable = missing-module-docstring
import os
import random
from flask import Flask, render_template, url_for
from tmdb import movie_search
from wiki import wiki_search


# create a flask object with variable name app
app = Flask(__name__)


@app.route('/')
#pylint: disable = missing-function-docstring
# def index function
# displays the index page accessible at "/"
def index():

    # initialize movie list with the specified id's
    movies_list = [70981, 299534, 634649, 207703, 566525]

    # python random choice() method returns a random element from a list
    # in this case, list is from movies_list
    random_mov = random.choice(movies_list)

    # here we are calling the function movie_search that we declared in tmdb.py
    # this will get all the neccessary information using the tmdb api such as
    # the title, tagline, genres, and movie image
    movie_info = movie_search(random_mov)

    wiki = wiki_search(movie_info['title'])

    # render_template is a flask function that is used to generate
    # output from a template file based on the Jinja 2 engine that is found
    # in the application template's folder
    return render_template("index.html", movie_info=movie_info, wiki=wiki)


@app.route
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=os.getenv("PORT", "8080"),
    debug=True
)
