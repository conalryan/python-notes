#!/usr/bin/env python

"""
Without using the class statement, create a class named SillyString, which is initialized with any string. Include an instance method called every_other which returns every other character of the string.

Instantiate your string and print the result of calling the every_other() method. Your test code should look like this:
  ss = SillyString('this is a test')
  print(ss.every_other())

It should output
ti sats
"""

def __init__(self, any_string):
    self.any_string = any_string


def every_other(self):
    return self.any_string[0::2]


SillyString = type("SillyString", (object,), {
    '__init__': __init__,
    'every_other': every_other
})


ss = SillyString('this is a test')

print(ss.every_other())