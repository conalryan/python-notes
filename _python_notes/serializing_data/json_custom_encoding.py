#!/usr/bin/env python

import json
from datetime import date


# Sample user-defined class (not JSON-serializable)
class Parrot():

    def __init__(self, name, color):
        self._name = name
        self._color = color

    # JSON does not understand arbitrary properties
    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color


# List of Parrot objects
parrots = [
    Parrot('Polly', 'green'), #
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]


# Custom JSON encoder function
def encode(obj):

    # Check for date object
    if isinstance(obj, date):

        # Convert date to string
        return obj.ctime()

    # Check for Parrot object
    elif isinstance(obj, Parrot):

        # Convert Parrot to dictionary
        return {'name': obj.name, 'color': obj.color}

    # If not processed, return object for JSON to parse with default parser
    return obj


# Dictionary of arbitrary data
data = {
    'spam': [1,2,3],
    'ham': ('a', 'b', 'c'),
    'toast': date(2014, 8, 1),
    'parrots': parrots,
}

# Convert Python data to JSON data
# 'default' parameter specifies function for custom encoding
# 'indent' parameter says to indent and add newlines for readability
print(json.dumps(data, default=encode, indent=4))

