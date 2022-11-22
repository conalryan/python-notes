#!/usr/bin/env python

"""
List Comprehensions
    Filters or modifies elements
    Creates new list
    Shortcut for a for loop

# Loop like this:
results = []
for var in sequence:
    results.append(expression)  # Where expression involves var

# Can be rewritten as:
results = [expression for var in sequence]

# Conditional if can be added to filter values:
results = [expression for var in sequence if expression]
"""
print('--> list comprehension')

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']
values = [2, 42, 18, 92, "boom", ['a', 'b', 'c']]

# Copy each fruit to upper case
upper_case_fruits = [fruit.upper() for fruit in fruits]
print("upper_case_fruits:", " ".join(upper_case_fruits))

# Select each fruit if it starts with 'a'
fruits_start_with_a = [fruit for fruit in fruits if fruit.startswith('a')]
print("fruits_start_with_a:", " ".join(fruits_start_with_a))

# Copy each number doubling it
doubles = [v * 2 for v in values]
print("doubles:", end=' ')
for d in doubles:
    print(d, end=' ')