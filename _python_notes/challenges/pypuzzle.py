#!/usr/bin/env python

from struct import Struct

"""
The file puzzle.data has a well-known name encoded in it.
The ASCII values of the characters in the name are represented by a series of integers and floats of various sizes.
The layout is:
    float, int, float, int, float, short, unsigned short, float, unsigned int, double, float, double, unsigned int, int, unsigned int, short

To decode, read the file into a bytes object and use a Struct object to decode the raw data into the values.
Then convert the values into integers, and use chr() to convert the integers into ASCII characters. 
Finally, you can join the characters together and print them out.
"""
s = Struct('fifif hHfId fdIiI h')

with open('data/puzzle.data', 'rb') as puzzle_in:
    puzzle_data = puzzle_in.read()
    (f1, i1, f2, i2, f3,
     i3, i4, f4, i5, d1,
     f5, d2, i6, i7, i8, i9) = s.unpack(puzzle_data)

    as_string = ''
    for item in f1, i1, f2, i2, f3, i3, i4, f4, i5, d1, f5, d2, i6, i7, i8, i9:
        as_int = int(item)
        as_string += chr(as_int)

    print(as_string)
