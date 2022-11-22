#!/usr/bin/env python

from president import President

"""
Write a main script to exercise some or all of the properties from president.py. 
It could look something like
    from president import President
    
    p = President(1)   # George Washington
    print("George was born at {0}, {1} on {2}".format(
        p.birth_place, p.birth_state, p.birth_date
    )
"""
with open('data/presidents.txt') as pres_in:
    for line in pres_in:
        print(line)
        p = President(line[0])