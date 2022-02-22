#pylint: disable = missing-module-docstring

import os
import requests
from dotenv import load_dotenv, find_dotenv

#pylint: disable = missing-module-docstring

# This is to load your API keys from .env
load_dotenv(find_dotenv())


#pylint: disable = missing-function-docstring

#def movie_search function with movie as our parameter
def movie_search(movie):

    #create a variable for our API endpoint
    #which is essentially the address of a particular data we want
    url = f"https://api.themoviedb.org/3/movie/{movie}"

    # intialize the parameters
    # os.getenv() method returns the value of the environmental variable key which in this case is TMDB_KEY
    query_params = {
        "api_key": os.getenv("TMDB_KEY"),
    }

    # the get() method sends a GET request to the specific URL and params
    response = requests.get(url, params=query_params)

    # whenever we make a request to a specified URL through Python, it returns
    # a response object. Now, this response object would be used to access certain features such as
    # content, headers, etc.

    # set the variable movie_info to response.json()
    # json() method of a response interface take a response strean and reads it to completion.
    movie_info = response.json()

    # set genre_info  to movie_info (which is our response that we are going to fetch)
    # in this case ['genres']
    genre_info = movie_info['genres']

    # make an empty list for genres
    genres = []

    # use a for loop to loop through each genre and append
    # the genre's ["name"] into the list we made beforehand
    for genre in genre_info:
        genres.append(genre["name"])

    # in order to generate a fully working image URL, we need 3 pieces of data.
    # those pieces are base_url, a file_size, and a file_path. This image_link variable
    # contains 2 of the 3 conditions we are looking for
    image_link = "https://image.tmdb.org/t/p/w500/"

    # our responses that we are going to fetch from movie_info
    # such as our title, tagline, genres, and image
    info = {
        "title": movie_info['title'],
        "tagline": movie_info['tagline'],
        'genres': genres,
        "image": image_link+movie_info['poster_path']
    }

    # returns info
    return info
