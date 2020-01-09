#!/usr/bin/env python

import inspect

"""
Inspect Module
    Simplifies access to metadata
    Provides user friendly functions for accessing Python metadata
    
Function(s)                         Description
------------------------------------------------
ismodule(),                         check object types
isclass(),
ismethod(),
isfunction(),
isgeneratorfunction(),
isgenerator(),
istraceback(),
isframe(),
iscode(),
isbuiltin(),
isroutine()
------------------------------------------------
getmembers()                        get members of an object that satisfy a given condition
------------------------------------------------
getfile(),                          find an object’s source code
getsourcefile(),
getsource()
------------------------------------------------
getdoc(),                           get documentation on an object
getcomments()
------------------------------------------------
getmodule()                         determine the module that an object came from
getclasstree()                      arrange classes so as to represent their hierarchy
------------------------------------------------
getargspec(),                       get info about function arguments
getargvalues()
------------------------------------------------
formatargspec(),                    format an argument spec
formatargvalues()
------------------------------------------------
getouterframes(),                   get info about frames
getinnerframes()
------------------------------------------------
currentframe()                      get the current stack frame
------------------------------------------------
stack(),                            get info about frames on the stack or in a traceback
trace()
"""
# Define a class
class Spam:
    pass


# Define a function
def Ham(p1, p2='a', *p3, p4, p5='b', **p6):
    pass


for thing in (inspect, Spam, Ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        # Test for module
        inspect.ismodule(thing),
        # Test for function
        inspect.isfunction(thing),
        # Test for class
        inspect.isclass(thing)
    ))

print()

# Get argument specifications for a function
print("Function spec for Ham:",inspect.getfullargspec(Ham))
print()

# Get frame (function call stack) info
print("Current frame:",inspect.getframeinfo(inspect.currentframe()))
