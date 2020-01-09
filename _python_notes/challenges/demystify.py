#!/usr/bin/env python

"""
Print out every third byte (starting with first byte) fo the file named mystery.
Output will be an ASCII picture.

Tip:
Read the file into a bytes object (Be sure to use binary mode),
then use slice notation to select the bytes,
then decode into a string for printing.
"""

with open('data/mystery', 'rb') as bytes_in:
    chunks = bytes_in.read()
    third_chunks = chunks[::3]
    print(third_chunks.decode())
