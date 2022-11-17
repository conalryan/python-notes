#!/usr/bin/env python

FRUITS = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
"ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
"Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
 "grape" ]


"""
sorted(<something>)
    Sorted returns a new list
    It defaults to sorting by ASCII (i.e. it will be case sensitive too)
    Stable sort
"""
print('--> sorted()')

# Default sort for strings is ASCII
sorted_fruits = sorted(FRUITS)
print(sorted_fruits)


"""
Custom sort keys
    Use key parameter
    Specify name of function to use
    Key function takes exactly one parameter
    Useful for case-insensitive sorting, sorting by external data, etc.

key
    Function to be executed once for each element of the list being sorted to provide the comparison values
    Function takes exactly one parameter (which is the element of the sequence being sorted) and return either a single value or tuple of values
    Returned values will be compared in order

example
    sorted_stuff = sorted(unsorted_stuff, key=some_function)
"""
print('--> sort key')


# Parameter is one element of iterable to be sorted
def ignore_case(e):
    # Return value to sort on
    return e.lower()


# Specify function with named parameter key
fruits_sorted = sorted(FRUITS, key=ignore_case)
print("Ignoring case:")
print(" ".join(fruits_sorted), end="\n\n")


def by_length_then_name(e):
    # Key functions can return tuple of values to compare in order
    return len(e), e.lower()


fruits_double_sorted = sorted(FRUITS, key=by_length_then_name)
print("By length, then name:")
print(" ".join(fruits_double_sorted))


NUMS = [800, 80, 1000, 32, 255, 400, 5, 5000]

# Numbers sort numerically by default
nums_sorted = sorted(NUMS)
print("Numbers sorted numerically:")
for n in nums_sorted:
    print(n, end=' ')
print("\n")

# Sort numbers as strings
nums_sorted_as_strings = sorted(NUMS, key=str)
print("Numbers sorted as strings:")
for n in nums_sorted_as_strings:
    print(n, end=' ')


"""
Sort by Title
    Remove articles (The, A, An) from title
"""
import re

books = [
    "A Study in Scarlet",
    "The Sign of the Four",
    "The Hound of the Baskervilles",
    "The Valley of Fear",
    "The Adventures of Sherlock Holmes",
    "The Memoirs of Sherlock Holmes",
    "The Return of Sherlock Holmes",
    "His Last Bow",
    "The Case-Book of Sherlock Holmes",
]

# Compile regex to match leading articles
rx_article = re.compile(r'^(the|a|an)\s+', re.I)


# Key function that takes element to compare and returns comparison key
def strip_articles(title):
    # Strip off article and convert title to lower case
    stripped_title = rx_article.sub('', title.lower())
    return stripped_title


# Sort using custom function
for book in sorted(books, key=strip_articles):
    print(book)