#!/usr/bin/env python

import re

"""
Set Comprehension
    Expression is added to set
    Transform iterable to set - with modifications
    Useful for turning any sequence into a set
    Items can be modified of skipped as the set is built
    If don't need to modify the items, it's probably easier to just pass the sequence to the set() constructor
"""
print('--> set comprehenesion')

with open("data/mary.txt") as mary_in:
    # Get unique words from file. Only one line is in memory at a time. Skip empty words.
    s = {w.lower() for ln in mary_in for w in re.split(r'\W+', ln) if w}
print(s)