#!/usr/bin/env python

from functools import wraps

"""
Write a decorator to double the return value of any function.
If a function returns 5, after decoration it should return 10.
If it returns "spam", after decoration it should return "spamspam", etc.
"""


# "inner decorator" - receives function being decorated
def deco(old_func):

    # Wrapper to retain name, properties, etc. of original function
    @wraps(old_func)
    def new_func(*args, **kwargs):  # Replacement function that is called instead of original
        # Call original function and get return value
        result = old_func(*args, **kwargs)
        # Multiple result of original function by multiplier
        return result * 2

    # Return the new function
    return new_func


# Apply the decorator to a function
@deco
def double(value):
    return value


# Call the new function
d = double(5)
print(d)

s = double("spam")
print(s)
