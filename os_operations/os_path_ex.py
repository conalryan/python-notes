#!/usr/bin/env python

import sys
import os

"""
os.path
    .abspath()
    .basename
    .dirname()  # File or folder name
    .getmtime()
    .getsize()
    .isdir()
    .isfile()
    .join()
    .exists()
"""
unix_p1 = "bin/spam.txt"  # Relative path
unix_p2 = "/usr/local/bin/ham"  # Absolute path

win_p1 = r"spam\ham.doc"  # Relative path
win_p2 = r"\\spam\ham\eggs\toast\jam.doc"  # Windows UNC path

if sys.platform == 'win32':
    print("win_p1:", win_p1)
    print("win_p2:", win_p2)
    print("dirname(win_p1):", os.path.dirname(win_p1))
    print("dirname(win_p2):", os.path.dirname(win_p2))
    print("basename(win_p1):", os.path.basename(win_p1))
    print("basename(win_p2):", os.path.basename(win_p2))
    print("isabs(win_p1):", os.path.isabs(win_p1))
    print("isabs(win_p2):", os.path.isabs(win_p2))
    print("isdir(win_p1):", os.path.isdir(win_p1))
    print("isdir(win_p2):", os.path.isdir(win_p2))
    print("isfile(win_p1):", os.path.isfile(win_p1))
    print("isfile(win_p2):", os.path.isfile(win_p2))
else:
    print("unix_p1:", unix_p1)
    print("unix_p2:", unix_p2)
    print("dirname(unix_p1):", os.path.dirname(unix_p1))
    print("dirname(unix_p2):", os.path.dirname(unix_p2))
    print("basename(unix_p1):", os.path.basename(unix_p1))
    print("basename(unix_p2):", os.path.basename(unix_p2))
    print("isabs(unix_p1):", os.path.isabs(unix_p1))
    print("isabs(unix_p2):", os.path.isabs(unix_p2))
    print("isdir('./data'):", os.path.isdir('./data'))
    print("isdir(./data/some_file.txt'):", os.path.isdir('./data/some_file.txt'))
    print("isfile(os.getcwd() + '/data'):", os.path.isfile('./data'))
    print("isfile('./data/some_file.txt'):", os.path.isfile('./data/some_file.txt'))
    print("getmtime('./data'):", os.path.getmtime('./data'))
    print("getmtime('./data/some_file.txt'):", os.path.getmtime('./data/some_file.txt'))

    print(
        'format("cp spam.txt {}".format(os.path.expanduser("~"))):',
        format("cp spam.txt {}".format(os.path.expanduser("~"))),
    )  # ~ is current user's home
    print(
        'format("cd {}".format(os.path.expanduser("~root"))):',
        format("cd {}".format(os.path.expanduser("~root"))),
    )  # ~NAME is NAME's home
