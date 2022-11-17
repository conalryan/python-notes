#!/usr/bin/env python

"""
Lambda Functions
    Short cut function definition
    Useful for functions only used in one place or creating a function on the fly
    Frequently passed as parameter to other functions (i.e. callback)
    Function body is an expression; it cannot contain other code
    Advantage of lambda function is solely the programmer's convenience. There is no speed or other advantage.
    One importance use of lambdas is for providing sort keys, another is for event handlers in GUIs.

Example:
    lambda parameter-list: expression

    # Lambda as normal function
    # But it's not possible to use the normal syntax as a function parameter, or as an element in a list.
    def function-name(parameter-list):
        return expression
"""
print('--> lambda')

fruits = ['watermelon','Apple','Mango','KIWI','apricot','LEMON','guava']

# Lambda takes one fruit and returns it in lower case
sorted_fruits = sorted(fruits, key=lambda e: e.lower())
print(" ".join(sorted_fruits))