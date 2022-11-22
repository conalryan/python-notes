#!/usr/bin/env python

"""
Monkey Patching
    Modify existing class or object by adding, replacing, or deleting attributes from outside the object's class defintion
    Useful for enabling/disabling behavior
        Replacing methods, attributes, or functions
        Modifying a third-party object for which you do not have access
        Adding behavior to objects in memory
    Can cause problems and hard to debug problems
        If the object being patched changes after a software upgrade, monkey patch can fail in unexpected ways
        Conflicts may occur if two different modules monkey-patch the same object
        Users of a monkey-patched object may not realize which behavior is original and which comes form the monkey patch
    Monkey patching defeats object encapsulation, and so it should be used sparingly!

"""
# Create normal class
class Spam(object):
    
    def __init__(self,name):
        self._name = name

    # Add normal method
    def eggs(self):
        print("Good morning, {}. Here are your delicious fried eggs.".format(self._name,))


# Create instance of class
s = Spam('Mrs. Higgenbotham')
# Call method
s.eggs()


# Define new method outside of class
def scrambled(self):
    print("Hello, {}. Enjoy your scrambled eggs".format(self._name,))


# Monkey patch the class with the new method
setattr(Spam, "eggs", scrambled)

# Call the monkey-patched method from the instance
s.eggs()
