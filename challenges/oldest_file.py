#!/usr/bin/env python

import sys, os

"""
Given a directory on the command line, print out the oldest file in that directory.
"""
path = sys.argv[1]

contents = os.listdir(path)

oldest = 0

for content in contents:
    try:
        time = os.path.getmtime(content)
        if time > oldest:
            oldest = content
    except FileNotFoundError as err:
        pass

print(oldest)