#!/usr/bin/env python

"""
Read presidents.txt, creating a list of president's last names.
Use list comprehension to make a copy of the list of names in upper case.
Loop through list and print otu the names one per line
"""
with open('data/presidents.txt') as pres_in:
    for line in pres_in:
        split = line.split(':')
        names = [name.upper() for name in split]
        print(names[1])