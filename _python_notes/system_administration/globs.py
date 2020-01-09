#!/usr/bin/env python

from glob import glob

"""
Glob
    Expands wildcards
    Windows and non-windows
    Useful with subprocess module
"""
# Expand file name wildcard into sorted list of matching names
files = glob('data/*.txt')
print(files)
