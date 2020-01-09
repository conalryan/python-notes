#!/usr/bin/env python

from dateutil import parser

"""
Print out the presidents sorted by the age at which they took office, youngest first.
"""

items = []

with open('data/presidents.txt') as pres_in:
    for line in pres_in:
        item = line.split(':')
        dob = parser.parse(item[3])
        in_office = parser.parse(item[7])
        age = in_office - dob
        item[-1] = age.days / 365
        items.append((item[-1], item[1]))


def getkey(item):
    return item[0]


for age, name in sorted(items, key=getkey):
    print(name, age)