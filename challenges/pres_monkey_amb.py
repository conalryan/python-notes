#!/usr/bin/env python

from president import President

"""
Monkey-patch the President class to add a method get_full_name which returns a single string consisting of the first name and the last name, separated by a space.
Try This_: Instead of a method, make full_name a property.
"""

@property
def full_name(self):
    return f"{self.first_name}-{self.last_name}"


setattr(President, "full_name", full_name)

p = President(1)
print(p.full_name)