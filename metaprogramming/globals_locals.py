#!/usr/bin/env python

# Import prettyprint function
from pprint import pprint

"""
globals() and locals()
    Contain all variables in a namespace
    globals()
        Returns a dictionary of all global objects
        Keys are the object names
        Values are the objects values
        Dictionary is 'live'; meaning changes to the dictionary affect global variables
    locals()
        Returns a dictionary of all objects in local scope
        Keys are the object names
        Values are the objects values
        Dictionary is 'live'; meaning changes to the dictionary affect global variables
"""
# Global variable
spam = 42
ham = 'Smithfield'


# Function parameters are local
def eggs(fruit):

    # Local variables
    name = 'Lancelot'
    idiom = 'swashbuckling'

    # globals() returns dict of all globals
    print("Globals:")
    pprint(globals())
    print()

    # locals() returns dict of all locals
    print("Locals:")
    pprint(locals())


eggs('mango')

"""
Prints
Globals:
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'metaprogramming/globals_locals.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10aacf390>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'eggs': <function eggs at 0x10aa54e18>,
 'ham': 'Smithfield',
 'pprint': <function pprint at 0x10aca99d8>,
 'spam': 42}

Locals:
{'fruit': 'mango', 'idiom': 'swashbuckling', 'name': 'Lancelot'}
"""