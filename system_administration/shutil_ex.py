#!/usr/bin/env python

import shutil
import os

"""
Using shutil module
    Portable ways to copy, move, and delete files
    Create archives
        zip file
        Compress tar archive of a folder
    Misc utilities
    Include several variations to specify attributes like file, etc.
"""
# Copy file
shutil.copy('data/alice.txt', 'betsy.txt')

print("betsy.txt exists:", os.path.exists('betsy.txt'))

# Rename file
shutil.move('betsy.txt', 'fred.txt')
print("betsy.txt exists:", os.path.exists('betsy.txt'))
print("fred.txt exists:", os.path.exists('fred.txt'))

new_folder = 'remove_me'

# Create new folder
os.mkdir(new_folder)
print("{} exists:".format(new_folder), os.path.exists(new_folder))
shutil.move('fred.txt', new_folder)

# Make a zip archive of new folder
shutil.make_archive(new_folder, 'zip', new_folder)
print("{}.zip exists:".format(new_folder), os.path.exists(new_folder + '.zip'))

# Recursively remove folder
shutil.rmtree(new_folder)
print("{} exists:".format(new_folder), os.path.exists(new_folder))
