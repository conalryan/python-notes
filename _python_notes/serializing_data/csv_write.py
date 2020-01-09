#!/usr/bin/env python

import sys
import csv

data = (
    ('February', 28, 'The shortest month, with 28 or 29 days'),
    ('March', 31, 'Goes out like a "lamb"'),
    ('April', 30, 'Its showers bring May flowers'),
)

with open('stuff.csv', 'w') as STUFF:
    if sys.platform == 'win32':
        # Create CSV writer from file object that is opened for writing
        # Note: On windows, need to set output line terminator to '\n'
        wtr = csv.writer(STUFF, lineterminator='\n')
    else:
        # Create CSV writer from file object that is opened for writing
        wtr = csv.writer(STUFF)
    for row in data:
        # Write one row (of iterables) to output file
        wtr.writerow(row)
