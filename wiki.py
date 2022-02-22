#pylint: disable = missing-module-docstring
import requests

#pylint: disable = missing-function-docstring


def wiki_search(movie):

    # create a variable for our the API endpoint
    # which is essentially the address of a particular data we want
    url = "https://en.wikipedia.org/w/api.php"

    # here we are initializing the parameters for our Wikipedia
    # API search
    params = {
        "action": 'query',
        "titles": movie,
        "format": 'json',
        "formatversion": 2,
    }

    # the get method sends a GET request to the specific URL and params
    response = requests.get(url, params=params)

    # json() method of a response interface takes a response stream
    # and reads it to completion
    response_json = response.json()

    # we set the query variable to response_json['query]
    # which will fetch data from and about MediaWiki
    query = response_json['query']

    # we set the pages variable to query['pages]
    # which will fetch pages
    pages = query['pages']

    # set first_page to pages[0] to fetch the first page
    first_page = pages[0]

    page_id = first_page['pageid']

    url = f"https://en.wikipedia.org/?curid={page_id}"

    return url
