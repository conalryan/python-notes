#!/usr/bin/env python

import sys

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json

"""
Consuming Web Services
    Use urllib.parse to URL encode the query
    Use urllib.request.Request
    Specify data type in header
    Open URL with urlopen Read data and parse as needed
    
    For URL encoding the query, use urllibparse.urlencode()
    It takes either a dictionary or an iterable of key/value paris, and returns a single string int he format "k1=V1*K2=V2*..." suitable for appending to a URL.
    
    Pass Request object to urlopen() and it will return a file-like object which you can read by calling its read() method.
    
    Data will be bytes object, so to use it as a string, call decode() on the data.
    
    List of public RESTful API: http://www.programmableweb.com/apis/directory/1? protocol=REST
"""
DATA_TYPE = 'application/json'

# Base URL of resource site
BASE_URL = 'http://lcboapi.com/products'
AUTH_TOKEN = 'CJAssociatesTraining'
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'


def main(args):

    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    search_term = args[0]

    setup_auth()

    params = make_params(search_term)

    # Build search URL
    url = BASE_URL + '?' + params

    do_query(url)


def do_query(url):
    # Send HTTP request and get HTTP response
    response = urllib.request.urlopen(url)
    # Read content from web site and decode() from bytes to str
    json_string = response.read().decode()

    # Convert JSON string to Python data strucutre
    raw_data = json.loads(json_string)
    # print('RAW JSON:', raw_data, '\n\n')
    # Check for results
    if raw_data['result']:
        for result in raw_data['result']:
            print("PRODUCT NUMBER:", result['product_no'])
            print("NAME:", result['name'])
            print("PACKAGE:", result['package'])
            print("PRICE: ${:5.2f}/liter".format(result['price_per_liter_in_cents']/100))
            print()
    else:
        print("Sorry, no items matched your query.")


def make_params(term):
    query_terms = {'q': term}
    # Create URL-encode string from query term(s)
    return urllib.parse.urlencode(query_terms)


def setup_auth():
    # Create password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # Add credentials to password manager
    password_mgr.add_password(None, BASE_URL, AUTH_TOKEN, AUTH_KEY)
    # Create authentication handler
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    # Create HTTP opener from password manager
    opener = urllib.request.build_opener(auth_handler)
    # Install HTTP opener to urllib.request
    urllib.request.install_opener(opener)


if __name__ == '__main__':
    # Remove the file name, and pass all args after that.
    main(sys.argv[1:])
