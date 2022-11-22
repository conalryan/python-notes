#!/usr/bin/env python

"""
Example module.
"""


def spam():
    print("Hello from spam()")


def ham():
    print("Hello from ham()")


# Use underscore to indicate that this method should not be used externally.
# Interpreter will not let you import anything that starts with an underscore.
def _eggs():
    print("Hello from _eggs()")

