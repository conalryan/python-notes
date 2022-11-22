#!/usr/bin/env python

import sys

"""
Command line args:
    - Accessed through sys.argv
    - sys.argv[0] is the file name
    - Slice out file name:
    ````py
    args = sys.argv[1:]    
    ````
    
    - Usage:
    ````bash
    python3 cmd_line_args.py apple mango
    ````
"""
print(sys.argv)  # ['cmd_line_args.py', 'apple', 'mango']

name = sys.argv[1]
print("name is", name)  # name is apple
