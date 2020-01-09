#!/usr/bin/env python

import sys
import os

"""
Permissions
    Simplest is os.access()
    Get mode form os.lstat()
    Use binary AND with permission constants
    inode
        Each entry in a Unix filesystem has a inode.
        Contains low-level information for the file, directory, or other filesystem entity.
    mode
        Permissions stored in the mode
        16 bit unsigned integer
            First 4 bits indicate what kind of entry it is
            Last 12 bits are the permissions
    os.access()
        Returns if file or directory is readable, writable, or executable
    os.lstat()
        Test for specific permission
        Returns tuple of inode data
    S_IMODE()
        Returns mode information as a number
    Predefined constants
        stat.S_IRUSR
        stat.IWGRP
    
"""
if len(sys.argv) < 2:
    sys.stderr.write('Please specify a starting directory\n')
    sys.exit(1)

start_dir = sys.argv[1]

# os.listdir() lists the contents of a directory
for base_name in os.listdir(start_dir):
    file_name = os.path.join(start_dir, base_name)

    # os.access() returns True if file has specified permissions
    #   os.W_OK
    #   os.R_OK
    #   os.X_OK
    #   combined with | (OR))
    if os.access(file_name, os.W_OK):
        print(file_name, "is writable")
