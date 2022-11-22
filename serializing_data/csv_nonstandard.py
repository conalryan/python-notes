#!/usr/bin/env python

import csv

with open('data/computer_people.txt') as computer_people_in:

    # Create CSV reader from open file object
    rdr = csv.reader(computer_people_in, delimiter=';')

    # Iterate over rows of data — csv reader is a generator
    for first_name, last_name, known_for in rdr:
        print('{}: {}'.format(last_name, known_for))

