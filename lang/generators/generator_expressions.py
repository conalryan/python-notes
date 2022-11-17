#!/usr/bin/env python

"""
Generator Expressions
    Like list comprehensions, but create a generator object.
    List comprehension returns complete list, generator returns one item at a time.
    More efficient
    Useful with functions like sum(), min() and max() that reduct an iterable input to a single value
    Use parentheses rather than brackets
        (expression for var in iterable)
"""
print('--> generator expression')

# Sum the squares of a list of numbers

# List comprehension: Entire list is stored in memory
list_comprehension_sum = sum([x*x for x in range(10)])
print(list_comprehension_sum)

# Generator expression: Only one square is in memory at a time
generator_expression_sum = sum(x*x for x in range(10))
print(generator_expression_sum)


page = open("data/mary.txt")
# Generator expression: Only one line in memory at a time. max() iterates over generated values.
max_line_length = max(len(line) for line in page)
page.close()
print(max_line_length)
