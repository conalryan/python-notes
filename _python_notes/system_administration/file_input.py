#!/usr/bin/env python

import fileinput

# fileinput.input() is a generator of all lines in all files in sys.argv[1:]
for line in fileinput.input():
    if 'bird' in line:
        # fileinput.filename() has the name of the current file
        print('{}: {}'.format(fileinput.filename(), line), end=' ')

