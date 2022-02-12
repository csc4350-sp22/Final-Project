#pylint: disable = missing-module-docstring
import requests

#pylint: disable = missing-function-docstring


def wiki_search(movie):

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": 'query',
        "titles": movie,
        "format": 'json',
        "formatversion": 2,
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    query = response_json['query']
    pages = query['pages']
    first_page = pages[0]
    page_id = first_page['pageid']
    url = f"https://en.wikipedia.org/?curid={page_id}"
    return url
