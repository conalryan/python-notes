#!/usr/bin/env python

"""
Control Flow Statements
    Loops
        for
        while
    List comprehensions
"""

FRUITS = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


"""
For Loops
    for a_variable in some_list:
        # do stuff with a_variable
    'break' keyword to stop iteration
    'continue' move to next iteration
    'else' block always called unless a break is hit
"""
a_list = ["value1", "two", "three"]
for item in a_list:
    print(item)

# break
for item in a_list:
    print(item)
    if item == "two":
        break

# continue
for item in a_list:
    if item == "two":
        continue
    print(item)

# else
for fruit in FRUITS:
    if fruit.startswith('b'):
        print(fruit)
        break
else:
    print('Not found')

# range()
# converts arg into list
# supports 3 args
#   range(5,10) # starts at 5 and goes to 9
#   range(5,10,2) # starts at 5, increments by 2 and goes to 9
x = 0
for index in range(10):
    x += 10
    print(x)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)


"""
While Loops
while some_condition == true:
    # do stuff
    # negate some_condition or increment/decrement counter
Check condition before we enter loop
Not used that much
'else' block always called unless a break is hit
"""
x = 0
while x < 10:
    print(x)
    x += 1

# do while
# Doesn't really exists use break to exit infinite loop
expr = False
while True:
    print('yup still looping')
    if expr:
      break
    expr = True
