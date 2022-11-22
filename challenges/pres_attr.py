#!/usr/bin/env python

from president import President

"""
Instantiate the President class. Get the first name, last name, and party attributes using getattr().
"""

p = President(1)
print(p)

fname, lname, party = getattr(p, 'first_name'), getattr(p, 'last_name'), getattr(p, 'party')
print(fname, lname, party)