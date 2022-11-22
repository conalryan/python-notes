#!/usr/bin/env python

import sys
import requests

"""
requests module
    HTTP the easy way!
    See details of requests API at http://docs.python-requests.org/en/v3.0.0/api/#main- interface
"""
# Base URL of resource site
BASE_URL = 'http://lcboapi.com/products'

# Credentials
AUTH_TOKEN = 'CJAssociatesTraining'
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'


def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    # Send HTTP request and get HTTP response
    response = requests.get(BASE_URL, params={'q': args[0]}, auth=(AUTH_TOKEN, AUTH_KEY))

    if response.status_code == requests.codes.OK:
        # Convert JSON content to Python data structure
        raw_data = response.json()
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
    else:
        print("Sorry, HTTP response", response.status_code)


if __name__ == '__main__':
    main(sys.argv[1:])
