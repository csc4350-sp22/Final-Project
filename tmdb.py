# pylint: disable = missing-module-docstring

import os
import requests
from dotenv import load_dotenv, find_dotenv

# pylint: disable = missing-module-docstring

# This is to load your API keys from .env
load_dotenv(find_dotenv())


# pylint: disable = missing-function-docstring

# def movie_search function with movie as our parameter
def movie_search(movie):

    # create a variable for our API endpoint
    # which is essentially the address of a particular data we want
    url = f"https://api.themoviedb.org/3/movie/{movie}"

    # intialize the parameters

    query_params = {
        "api_key": os.getenv("TMDB_KEY"),
    }

    response = requests.get(url, params=query_params)
    movie_info = response.json()
    genre_info = movie_info["genres"]
    genres = []

    for genre in genre_info:
        genres.append(genre["name"])

    image_link = "https://image.tmdb.org/t/p/w500/"

    info = {
        "title": movie_info["title"],
        "tagline": movie_info["tagline"],
        "genres": genres,
        "image": image_link + movie_info["poster_path"],
    }

    # returns info
    return info
