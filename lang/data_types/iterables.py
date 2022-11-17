#!/usr/bin/env python

"""
Iterables
    Expression that can be looped over
    Can be collections e.g. list, tuple, str, bytes
    Can be generators e.g. range(), file objects, enumerate(), zip(), reversed()
        Generators does not keep all its values in memory - it creates them one at a time as needed, and feeds them to
        for-in loop (saves memory).
    Collections
        In memory
        Eager
        Sequences
            str
            bytes
            list
            tuple
            collections.namedtuple
            sorted()
            list comprehension
        Mappings
            dict
            set
            frozenset
            collections.defaultdict
            collections.Counter
            dict comprehension
            set comprehension

    Generators
        Virtual
        Lazy
        open()
        range()
        enumerate()
        DICT.items()
        zip()
        itertools.izip()
        generator expression
        generator function
        generate class
"""