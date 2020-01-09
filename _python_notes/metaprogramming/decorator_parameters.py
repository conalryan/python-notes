#!/usr/bin/env python

# Wrapper to preserve properties of original function
from functools import wraps

"""
Decorator Parameters
    A decorator can be passed parameters. This requires a little extra work.
    Require two nested functions
    Method call returns replacement function in classes
    Decorators functions
        The decorator itself is passed the parameters
        Contains nested function that is passed the decorated function (the target)
        Nested function returns the replacement function
    Decorator classes
        init is passed the parameters
        call is passed the decorated function (the target)
        call returns the replacement function
"""
# Actual decorator - receives decorator parameters
def multiply(multiplier):

    # "inner decorator" - receives function being decorated
    def deco(old_func):

        # Wrapper to retain name, properties, etc. of original function
        @wraps(old_func)
        def new_func(*args, **kwargs):  # Replacement function that is called instead of original
            # Call original function and get return value
            result = old_func(*args, **kwargs)
            # Multiple result of original function by multiplier
            return result * multiplier

        # Return the new function
        return new_func

    # Return the decorator
    return deco


@multiply(4)
def spam():
    return 5


@multiply(10)
def ham():
    return 8


a = spam()
b = ham()
print(a, b)
