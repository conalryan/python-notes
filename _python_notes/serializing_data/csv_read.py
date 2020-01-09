#!/usr/bin/env python

import csv

with open('data/knights.csv') as knights_in:

    #  Create CSV reader
    rdr = csv.reader(knights_in)

    # Read and unpack records one at a time; each record is a list
    for name, title, color, quest, comment, number, ladies in rdr:
        print('{:4s} {:9s} {}'.format(
            title, name, quest
        ))
