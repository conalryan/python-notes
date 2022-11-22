#!/usr/bin/env python

import requests

"""
requests module
    Pythonic front end to urllib, urllib2, httplib, etc
    Makes HTTP transactions simple
    urllib and firends are powerful but complex for non-trivial tasks.
    You have to do a lot of work if you want to provide authentication, proxies, headers, or data, etc.
    requests module is much simpler and included with Anaconda or is readily available from PyPI via pip.
"""
# request.get() returns HTTP response object
response = requests.get("https://www.python.org")

# response.headers is a dictionary of the headers
for header, value in sorted(response.headers.items()):
    print(header, value)
print()

# The test is returned as a bytes object, so it needs to be decoded to a string
print(response.content[:200].decode())   # Print the first 200 bytes
print('...')
print(response.content[-200:].decode())   # Print the last 200 bytes
