#!/usr/bin/env python

"""
Scripting for System Administration
    Launch external program
    Check permissions on files
    Get system configuration information
    Store data offline
    Parse command line options
    Create Unix-style filters
    Configure application logging

Creating a Useful Command line Script
    More than just some lines of code
    Input + Business Logic + Output
    Process files for input, or STDIN
    Allow options for customizing execution
    Log results

    Good admin script should gather data, apply appropriate business logic and output results of desired location.

argparse module
    Parsing options and parameters on the script's command line.

fileinput
    Simplifies processing a list of files specified on the command line.

logging module
   Output to a variety of log destinations
    Plain file
    syslog
    Unix-like systems
    NTLog service on Windows
    email

Creating Filters
    Filters read file or STDIN and writes to STDOUT
    Common on Unix systems well-known filters:
        awk
        sed
        grep
        head
        tail
        cat
    Reads command line arguments as files, otherwise STDIN use fileinput.input()
    Common script that iterates over all lines in all files specified on the command line.
        for filename in sys.argv[1:]:
            with open(filename) as F:
                for line in F:
                    # process line
    Many Unix utilities are written to work this way - sed, grep, awk, head, tail, sort, etc.
    They are called filters because they filter their input in some way and output the modified text.
    Such filters read STDIN if no files are specified, so that they can be piped into.

    fileinput.input() class
        Provides a shortcut for this kind of file processing.
        It implicitly loops through sys.argv[1:], opening and closing each file as needed, and then loops through the lines of each file.
        If sys.argv[1:] is emtpy then it reads sys.stdin.
        If a filename in the list is '-', it also reads sys.stdin.

        fileinput Methods
        Method          Description
        -----------------------------
        filename()      Name of current file being readable

        lineno()        Cumulative line number from all files read so far

        filelineno()    Line number of current file

        isfirstline()   True if current line is first line of a file

        isstdin()       True if current file is sys.stdin

        close()         Close fileinput
"""