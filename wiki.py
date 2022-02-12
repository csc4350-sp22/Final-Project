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
    wiki_search = response.json()
    query = wiki_search['query']
    pages = query['pages']
    first_page = pages[0]
    page_id = first_page['pageid']
    url = f"https://en.wikipedia.org/?curid={page_id}"
    return url
