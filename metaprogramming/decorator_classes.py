#!/usr/bin/env python

"""
Decorator Classes
    Same purpose as decorator functions
    Must implement two methods:
        __init__ method expects original function
        __call__ method replaces original function
"""
# Decorator implemented class
class debugger(object):

    # Original function passed into decorator's constructor
    def __init__(self, func):
        self._func = func

    # call() is replacement function
    def __call__(self, *args, **kwargs):

        # Add functionality to original function
        print("*" * 40)
        print("** function", self._func.__name__,"**")

        if args:
            print("\targs are ", args)
        if kwargs:
            print("\tkwargs are ", kwargs)

        print("*" * 40)

        # Call the original function
        return self._func(*args, **kwargs)


# Apply debugger to function
@debugger
def hello( greeting, whom="world"):
    print("{}, {}".format(greeting, whom))


# Call replacement function
hello('hello','world')
print()

hello('hi','Earth')
print()

hello('greetings')
