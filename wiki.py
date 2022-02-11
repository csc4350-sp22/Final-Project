import requests


def wiki_search(movie):
    URL = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": 'query',
        "titles": movie,
        "format": 'json',
        "formatversion": 2,
    }
    response = requests.get(URL, params=params)
    response_json = response.json()
    query = response_json['query']
    pages = query['pages']
    first_page = pages[0]
    page_id = first_page['pageid']
    link = f"https://en.wikipedia.org/?curid={page_id}"
    return link
