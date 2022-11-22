#!/usr/bin/env python

from datetime import datetime
import calendar

"""
Given dates below, print out the date, day of week it fell on and True if it occurs in leap year
else False
"""
d1 = datetime(1956, 10, 31)
d2 = datetime(1952, 9, 22)
d3 = datetime(1990, 8, 27)

for d in d1, d2, d3:
    print(d, d.strftime('%a'), calendar.isleap(d.year))