#!/usr/bin/python
# sorter.py 
# Conal Ryan
# 2/15/14

import argparse

parser = argparse.ArgumentParser(prog='Sorter', usage='string1 string2 [-r || --reverse]')

parser.add_argument('-r', '--reverse', action='store_true', help='reverse sort of the entered strings')
parser.add_argument('strings', nargs='+', help='enter two or more strings to sort')

args = parser.parse_args()

if len(args.strings) < 2:
    print "Please enter two or more strings to sort."
else:
    if args.reverse:
        args.strings.sort(reverse=True)
        print args.strings
    else:
        args.strings.sort()
        print args.strings