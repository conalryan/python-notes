#!/usr/bin/env python

import csv

# Field names, which will become dictionary keys on each row
field_names = ['term', 'firstname', 'lastname', 'birthplace', 'state', 'party']

with open('data/presidents.csv') as presidents_in:

    # Create reader, passing in field names (if not specified, uses first row as field names)
    rdr = csv.DictReader(presidents_in, fieldnames=field_names)

    # Iterate over rows in file
    for row in rdr:

        # **row converts row to individual parameters
        print('{firstname:25s} {lastname:12s} {party}'.format(**row))
