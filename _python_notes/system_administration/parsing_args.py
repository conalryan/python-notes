#!/usr/bin/env python

import re
import fileinput
import argparse
# Needed on Windows to parse filename wildcards
from glob import glob
# Needed on Windows to flatten list of filename list
from itertools import chain

"""
Parsing the Command Line
    sys.argv
        All arguments are available in Python via sys.argv
        Parse and analyze sys.argv
    argparse
        Parses entire command line
        Very flexible
        Validates options and arguments
        syntax
            arg_parser = argparse.ArgumentParser(description="Some description")
            arg_parser.add_argument(
                '-<some_flag>',
                dest='some_flag_name',
                action='store_true',
                help='some description'
            )
    Options
        Control behavior of the script
    Arguments
        Provide input (frequently file names, but can be anything)

    
add_argument() named parameters
parameter       description
----------------------------
dest            Name of attribute (defaults to argument name)

nargs           Number of arguments
                Default: one argument, returns string 
                '*': 0 or more arguments, returns list 
                '+': 1 or more arguments, returns list 
                '?': 0 or 1 arguments, returns list
                N: exactly N arguments, returns list

const           Value for options that do not take a user-specified value

default         Value if option not specified

type            type which the command-line arguments should be converted ; one of 'string', 'int', 'float', 'complex' or a function that accepts a single string argument and returns the desired object. (Default: 'string' )

choices         A list of valid choices for the option

required        Set to true for required options

metavar         A name to use in the help string (default: same as dest)

help            Help text for option or argument

Usage
    parsing_args.py -i '\bbil' data/alice.txt data/president.txt
"""
# Create argument parser
arg_parser = argparse.ArgumentParser(description="Emulate grep with python")

# Add option to the parser (dest is name of option attribute)
arg_parser.add_argument(
    '-i',
    dest='ignore_case',
    action='store_true',
    help='ignore case'
)

# Add required argument to the parser
arg_parser.add_argument(
    'pattern',
    help='Pattern to find (required)'
)

# Add optional argument to parser (nargs='*' means 0 or more arguments)
arg_parser.add_argument(
    'filenames',
    nargs='*',
    help='filename(s) (if no files specified, read STDIN)'
)

# Actually parse the arguments
args = arg_parser.parse_args()

print('-' * 40)
print(args)
print('-' * 40)

# Compile the pattern for searching; set re.IGNORECASE if -i option
regex = re.compile(args.pattern, re.I if args.ignore_case else 0)

# For each filename argument, expand any wildcards; this returns list of lists
filename_gen = (glob(f) for f in args.filenames)

# Flatten list of lists into a single list of files to process
# (Note: both filename_gen and filenames are generators; these two lines are only needed on Windows
# Non-Windows systesm automatically expand wildcards)
filenames = chain.from_iterable(filename_gen)

# Loop over list of file names and read them one line at a time
for line in fileinput.input(filenames):
    if regex.search(line):
        print(line.rstrip())

