#!/usr/bin/python
# Conal Ryan
# 2/14/15
# sorter3.py
# invoke $ python sorter3.py string1, string2, ...
# use -r or --reverse to sort descending

import sys, getopt

def main(argv):
    opts, args = getopt.getopt(argv, "r", ["reverse"])

    print opts
    print args
    
    if len(opts) > 0:
        args.sort(reverse=True)
        print args
    else:
        args.sort()
        print args

if len(sys.argv) > 1:
    main(sys.argv[1:])
else:
    print "Invalid command line arguments. Please supply two or more strings to sort"        
