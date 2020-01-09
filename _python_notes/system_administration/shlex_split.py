#!/usr/bin/env python

import shlex

"""
Using shlex.split()
    Splits string
    Preserves white space (quoted whitespace within a string)
    If you have an external command you want to execute, you should split it into individual words.
    If your command has quoted whitespace, the normal split() method of a string, won't work.
    
"""
# Command line with quoted whitespace
cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'

# Normal split does the wrong thing
print(cmd.split())
print()

# shlex.split() does the right thing
print(shlex.split(cmd))
