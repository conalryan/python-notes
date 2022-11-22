#!/usr/bin/env python

from datetime import datetime

"""
Calculate number of days between December 7, 1941 and Auguest 15, 1945
"""

d1 = datetime(1941, 12, 7, 0, 0, 0)
d2 = datetime(1945, 8, 15, 0, 0, 0)
dif = d2 - d1
print(dif.days)