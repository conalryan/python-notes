#!/usr/bin/env python

from datetime import datetime

"""
Print out all the presidents first and last names, date of birth, and their political affiliations, sorted by date of birth.
Read the presidents.txt file, putting the four fields into a list of tuples.
Loop through the list, sorting by date of birth, and printing the information for each president.
Use sorted() and a lambda function.
"""
with open('data/presidents.txt') as pres_in:

    pres = []
    for line in pres_in:
        split = line.split(':')
        first_name, last_name, dob, party = (split[2], split[1], split[3], split[-1])
        # Convert string to date
        y, m, d = dob.split('-')
        date_of_birth = datetime(int(y), int(m), int(d))
        print(date_of_birth)
        pres.append((first_name, last_name, date_of_birth, party))

    sort = sorted(pres, key=lambda e: e[2])

    for first_name, last_name, dob, party in sort:
        print(first_name, last_name, dob, party)