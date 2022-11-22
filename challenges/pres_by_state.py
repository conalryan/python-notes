#!/usr/bin/env python

"""
Using file presidents.txt, count the number of Presidents who were born in each state.
E.g.:
Arkansas 1
California 1
Connecticut 1
etc.

"""
data = {}

with open('DATA/presidents.txt') as pres_in:
    for line in pres_in:
        items = line.split(':')
        state = items[6]
        num = data.get(state, 0)
        num += 1
        data[state] = num

for k , v in sorted(data.items()):
    print(k, v)