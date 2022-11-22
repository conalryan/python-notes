#!/usr/bin/env python

import os

"""
List each component of you PATH environment variable with the number of files it contains.
This set of files can be executed from the command line without specifying their path.

e.g.
/usr/bin 2376
/usr/local/bin 17
etc.
"""

paths = os.environ.get('PATH')

for path in paths.split(':'):
    try:
        count = len(os.listdir(path))
        print(path, count)
    except FileNotFoundError as err:
        pass
