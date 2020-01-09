#!/usr/bin/env python

"""
Write a generator function to provide a sequence of the names of presidents
(in "FIRSTNAME MIDDLENAME LASTNAME" format) from the presidents.txt file.
They should be provided in the same order they are in the file.
You should not read the entire file into memory, but one-at-a-time from the file.
Then iterate over the the generator returned by your function and print the names.
"""

FILENAME = 'data/presidents.txt'


def pres_gen(filename):
    with open(filename) as pres_in:
        for line in pres_in:
            line_split = line.split(':')
            lname = line_split[1]
            name = line_split[2]
            fname = name.split(' ')[0]
            mname = ''
            try:
                mname = name.split(' ')[1]
            except IndexError as err:
                pass
            yield fname.upper(), mname.upper(), lname.upper()


for fname, mname, lname in pres_gen(FILENAME):
    print(fname, mname, lname)