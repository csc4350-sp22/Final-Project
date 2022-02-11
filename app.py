import os
import flask
import random
from tmdb import movie_search
from wiki import wiki_search


#make app object
app = flask.Flask(__name__)

#tells Flask what URL should triger our function
@app.route('/')

#def index function     
def index():
    
    #initialize movie list with the specified id's
    movies_list = [70981, 299534, 634649, 207703, 566525]

    #python random choice() method returns a random element from a list
    #in this case, list is (movies)
    random_mov = random.choice(movies_list)

    #movie_info will search for a random movie in movie_list
    #and store the data in movie_info
    movie_info = movie_search(random_mov)

    wiki = wiki_search(movie_info['title'])

    #render_template is a flask function that is used to generate
    #output from a template file based on the Jinja 2 engine that is found
    #in the application template's folder
    return flask.render_template("index.html", movie_info=movie_info, wiki=wiki)

app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT",8080)),
    debug=True
)
