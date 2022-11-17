#!/usr/bin/env python

"""
Variables
    - Names or labels pointing to/referencing a memory location.
    - Names must be a-z A-Z 0-9 _
    - Dynamically typed.
    - Type is determined by assignment.
"""
x = 5
y = 10
result = x + y
print(result)  # 15

# Dynamically typed so type will change on new assignment.
x = "Bob"
print(x)  # Bob
m = x
print(m)  # Bob
m = 42
print(m)  # 42

# Spam and ham are referencing same object.
spam = [ 'a', 'b', 'c']
ham = spam

# Update ham.
ham[0] = 'huh?'
# Spam is updated too.
print(spam)  # ['huh?', 'b', 'c']

print(spam is ham)  # True
print(id(spam) == id(ham))  # True

# To make a copy use list() or slice.
print('Copy')
toast = list(spam)
print(toast is spam)  # False

toast_slice = spam[:]
print(toast_slice is spam)  # False

# There is no point in having 2 objects for the same int, so Python reuses it.
i = 12
j = 12
print(i is j)  # True
print(id(i), id(j))  # 4370261680 4370261680 **Note** actual numeric value will change on each run.
