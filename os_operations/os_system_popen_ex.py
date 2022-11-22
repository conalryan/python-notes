#!/usr/bin/env python

import sys
import os

"""
os.system()
    Launches any external command as though you had typed it at a command prompt.
"""
os.system("hostname")
os.system("ls")


"""
os.popen()
    Opens a command, returning a file-like object.
    You can use any of the methods used for a file.
"""
with os.popen('netstat -an') as netstat_in:
    for entry in netstat_in:
        if 'ESTAB' in entry:
            print(entry, end='')
