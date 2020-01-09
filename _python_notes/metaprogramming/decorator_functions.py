#!/usr/bin/env python

from functools import wraps

"""
Decorator Functions
    Provide a wrapper around a function
    Add features/functionality to a function without changing the function itself
    Expects only one argument - the functino to be modified
    Returns a new function, which will replace the original.
    Replacement function typically calls the original function as well as some new code.
    The wraps decorator form the functools module in the standar library should be used with the function that returns the replacment function
    This makes sure the replacement function keeps the same properties (especially the anme) as the original (target) function.
    Syntax
        @decorator
        def function():
            pass
    Same as
        function = decorator(function)
"""
# Decorator function - expects decorated (original) function as a parameter
def debugger(old_func):

    # @wraps preserves name of original function after decoration
    @wraps(old_func)
    def new_func(*args, **kwargs):  # Replacement function; takes generic parameters
        # New functionality added by decorator
        print("*" * 40)
        print("** function", old_func.__name__,"**")

        # New functionality added by decorator
        if args:
            print("\targs are ", args)
        if kwargs:
            print("\tkwargs are ", kwargs)

        print("*" * 40)

        # Call the original function
        return old_func(*args, **kwargs)

    # Return the new function object
    return new_func


# Apply the decorator to a function
@debugger
def hello(greeting, whom='world'):
    print("{}, {}".format(greeting, whom))


# Call the new function
hello('hello', 'world')
print()

hello('hi', 'Earth')
print()

hello('greetings')

