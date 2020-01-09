#!/usr/bin/env python

# .dummy has Pool for threads
from multiprocessing.dummy import Pool
from pprint import pprint
import requests

POOL_SIZE = 8

# Credentials to acces site
AUTH_TOKEN = 'CJAssociatesTraining'
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

# Base url of site to access
BASE_URL = 'http://lcboapi.com/products'

# Terms to search for; each thread will search some of these terms
search_terms = [
    'stolichnaya', 'makers mark', 'woodford', 'wombat', 'molson', 'moosehead',
    'michelob', 'bacardi', 'old rotgut', 'four roses', 'moonshine', 'harvest',
    'captain morgan', 'tanqueray','green spot', 'chartreuse'
]


# Function invoked by each thread for each item in list passed to map()
def fetch_data(search_term):

    # Request sent to site
    response = requests.get(
        BASE_URL,
        auth=(AUTH_KEY, AUTH_TOKEN),
        params={'q': search_term},
    )

    # Convert JSON to Python structure
    raw_json = response.json()

    names = []
    if raw_json['result']:
        for result in raw_json['result']:
            names.append(result['name'])

    # Return all names that matched one search term
    return names


# Create pool of POOL_SIZE
p = Pool(POOL_SIZE)

# Launch threads, collect results
results = p.map(fetch_data, search_terms)

# Iterate over results, mapping them to search terms
for search_term, result in zip(search_terms, results):
    print("{}:".format(search_term.upper()))
    if result:
        pprint(result)
    else:
        print("** no results **")
