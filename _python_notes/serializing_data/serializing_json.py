#!/usr/bin/env python

"""
Serializing JSON

About JSON
    Lightweight, human-friendly format for data
    Contains dictionaries and lists
    Stands for JavaScript Object Notation
    Looks like Python
    Basic types: Number, String, Boolean, Array, Object
    Strings are enclosed in double quotes (only)
    A JSON file contains objects and arrays, which correspond exactly to Python dictionaries and lists.
    White space is ignored
    Stricter rules than Python
    It was developed and popularized by Douglas Crockford starting in 2001.

Reading JSON
    json module in standard library
    json.load() parse from file-like object
    json.loads() parse from string
    Both methods return Python dict or list

Writing JSON
    json.dumps()
        To output JSON to a string, use json.dumps().
    json.dump()
        To output JSON to a file, pass a file-like object to json.dump().
    In both cases, pass a Python data structure as the data to be output.

Customizing JSON
    JSON data types limited
    simple cases — dump dict
    create custom encoders
    The JSON spec only supports a limited number of datatypes.
    If you try to dump a data structure contains dates, user-defined classes, or many other types, the json encoder will not be able to handle it.
    Encoder
        You can a custom encoder for various data types.
        To do this, write a function that expects one Python object, and returns some object that JSON can parse, such as a string or dictionary.
        The function can be called anything.
        Specify the function with the default parameter to json.dump().
        The function should check the type of the object.
        If it is a type that needs specially handling, return a JSON-friendly version, otherwise just return the original object.

Python types that JSON can encode
Python          JSON
---------------------
dict            object

list            array

str             string

int             number (int)

float           number (real)

True            true

False           false

None            null

NOTE
    see the file json_custom_singledispatch.py for how to use the singledispatch module (which is not in the standard library) to handle multiple data types.
"""