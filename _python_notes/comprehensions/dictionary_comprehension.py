#!/usr/bin/env python

"""
Dictionary Comprehension
    Expression is key/value pair
    Transform iterable to dictionary
    If key is used more than once, it overrides any previous keys.
    Handy for building a dictionary from a sequence of values
"""
print('--> dictionary comprehension')

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# Create a dictionary with key/value pairs derived from an iterable
d = {a.lower(): len(a) for a in animals}
print(d)
