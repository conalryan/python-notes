#!/usr/bin/env python

"""
Working with Attributes
    All Python objects are dictionaries of attributes
    Special functions can be used to access attributes
    Attributes specified as strings
    Four special builtin functions for managing attributes
        getattr(object,  attribute [,defaultvalue])
            Returns the value of a specified attribtes, or None if the object does not have that attribute
            a.spam is the same as getattr(a, 'spam')
            Optional third argument to getattr() provides default value for nonexistent attributes
        hasattr(object, attribute)
            Returns the value of a specified attribute, or None if the object does not have that attribute
        setattr(object, attribute, value)
            Set an attribute to the specified value
        delattr(object, attribute)
            Deletes an attribute and its corresponding value

"""
class Spam(object):

    # Create attribute
    def eggs(self, msg):
        print("eggs!", msg)


s = Spam()

s.eggs("fried") # eggs! fried

# Check whether attribute exists
print("hasattr()", hasattr(s, 'eggs'))  # hasattr() True

# Retrieve attribute
e = getattr(s, 'eggs')
e("scrambled")  # eggs scrambled


def toast(self, msg):
    print("toast!", msg)


# Set (or overwrite) attribute
setattr(Spam, 'eggs', toast)

s.eggs("buttered!")  # toast! buttered!

# Remove attribute
delattr(Spam, 'eggs')

try:
    s.eggs("shirred")
except AttributeError as err:  # Missing attribute raises error
    print(err)  # 'Spam' object has no attribute 'eggs'

