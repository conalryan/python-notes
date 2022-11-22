#!/usr/bin/env python

import urllib.request

u = urllib.request.urlopen("https://www.python.org")

# info() returns a dictionary of HTTP headers
print(u.info())
print()

# Test is returned as bytes object, used decode() to convert to a string
print(u.read(500).decode())
