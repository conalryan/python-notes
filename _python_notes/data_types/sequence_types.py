#!/usr/bin/env python

import sys

"""
Sequence Types:
    - str
    - bytes
    - list
    - tuple
    All sequences share a common set of operations, methods, and builtin functions.
    Each type also has operations specific to that type.
    All sequences support slicing, which means returning a subset of the sequence using [start:*limit*:*step*]
"""


"""
str
    Strings
    Immutable sequence of Unicode codepoints (i.e. arrays of Unicode characters)
    Unicode text in Python 3 but ascii text in Python 2
    Single quotes, double quotes, triple quotes
    Triple quotes can be used for multi-line strings and is often used for documentation
    Convert string to bytes with encode()
    Convert bytes to string with decode()
"""
single_quotes = 'I have single quotes'

double_quotes = "I have double quotes"

triple_quotes= """I have triple quotes"""  # You can use double or single quotes

bytes_from_string = single_quotes.encode()
print(bytes_from_string)  # b'I have single quotes'


"""
Triple quotes used for documentation or multi line strings
"""
# Multi line strings
query = """
select *
from flights
where airline == 'Delta'
order by flight_time
"""


"""
Built-in String functions
"""
print('--> Built-in string functions')
some_string = "hello"
print(some_string.capitalize())  # Hello
print(some_string.replace("e", "a"))  # Hallo
print(some_string.isalpha())  # True
print("123".isnumeric())  # True  # useful when converting to int
print("some,csv,values".split(","))  # ['some', 'csv', 'values']

some_string = "Hello with a trailing space   .  "
some_string.rstrip() # Remove any trailing spaces, tabs, new lines
print(some_string)  # Hello with a trailing space   .


"""
Format
  {}
  {<an_int>} numbered placeholder is redundant since it reads left to right (e.g. {0} {1})
  Add width, padding
  Access elements of sequences and dictionaries
  Access object attributes
  
  {:d}      Format the argument as an integer +
  {:03d}    Format as an integer, 3 columns wide, zero padded +
  {:>25s}   Same but right-justified +
  {:.3f}    Format as a float, with 3 decimal places
"""
print('--> Format')
name = "Bob"
machine = "Bobot"
print("Nice to meet you {0}. I am {1}.".format(name, machine))  # Nice to meet you Bob. I am Bobot.

name = 'Bob'
city = 'Peabody'
print("{} is from {}".format(name, city))  # Bob is from Peabody

# Optional add number for placeholder, but it's redundant since it's always left to right.
print("{0} is from {1}".format(name, city))  # Bob is from Peabody

result = 34.3902 / 12.2920
print(result)  # 2.7977709079075823
print("{}".format(result))  # 2.7977709079075823
print("{:.2f}".format(result))  # 2.80

# Escape
print("spam\\n")  # spam\n

color = 'blue'
animal = 'iguana'

# Placeholders are auto-numbered, starting at 0
print('{} {}'.format(color, animal))

fahr = 98.6839832
# Float with 1 decimal place
print('{:.1f}'.format(fahr))  # 98.7

value = 12345
# Manually number placeholder to reuse it
print('{0:d} {0:04x} {0:08o} {0:016b}'.format(value))  # 12345 3039 00030071 0011000000111001

data = {'A': 38, 'B': 127, 'C': 9}

for letter, number in sorted(data.items()):
    # :4d means format decimal integer in a field 4 characters wide
    print("{} {:4d}".format(letter, number))  # A   38 B  127 C    9


"""
Interpolation
    f
        In front of string - place vars directly in brackets as of Python 3.6
        Shorter syntax for string formatting
    r
        Raw string
    u
        unicode
"""
print('--> Interpolation')
# f
print(f"{name} is from {city}")  # Bob is from Peabody
print(f"Nice to meet you {name}. I am {machine}")  # Nice to meet you Bob. I am Bobot.

x = 24
y = 32.2345
print(f"{x:10s}{y:.2f}")

# f strings are only supported in Python 3.6+
if sys.version_info.major == 3 and sys.version_info.minor >= 6:

    name = "Tim"
    count = 5
    avg = 3.456
    info = 2093
    result = 38293892

    # < means left justify (default for non-numbers), 10 is field width, s formats a string
    print(f"Name is [{name:<10s}]")
    # > means right justify
    print(f"Name is [{name:>10s}]")
    # .2f means round a float to 2 decimal points
    print(f"count is {count:03d} avg is {avg:.2f}")
    # d is decimal, o is octal, x is hex
    print(f"info is {info} {info:d} {info:o} {info:x}".format(info))
    # , means add commas to numeric value
    print(f"${result:,d}".format(result))

    city='Orlando'
    temp=85
    # Parameters can be selected by name instead of position
    print(f"It is {temp} in {city}")

else:
    print("Sorry -- f-strings are only supported by Python 3.6+")

# r
print(r"spam\n")  # spam\n

# u
print("80\u00B0 in Durham yesterday")  # 80° in Durham yesterday


"""
bytes
    Immutable sequence of bytes (i.e. arrays of bytes)
    Convert bytes to string with decode()
    Convert string to bytes with encode()
"""
print('--> bytes')
bits = b'data'
byts = b"data"
string_from_bytes = bits.decode()

# Stream of bytes (web page)
import requests

web_page = requests.get('http://www.amadeus.com')
print(web_page.content)  # will print a stream of bytes

print('abc')  # abc  # array of characters
print(b'abc')  # b'abc'  # array of bytes

name = 'Guido'
print(name.encode())  # b'Guido'  #  Defaults to UTF-8

data = b'1234'
print(data[0])  # 49  # ASCII code for the digit 1.
print(data.decode())  # 1234


"""
list
    Mutable sequence of objects
    Use a list when you have a collection of similar objects
    sequence[start:limit:stride]
    []
    [0] first index
    [-1] last index
    .append() to add to list my_list.append("some new value")
    'in' keyword to check if value is in the list
    'len' keyword to get the length of the list len(my_list)
    'del' keyword to remove item del my_list[2]
    [1:] Slice out first item
    [:-1] Slice out last item
"""
print('--> list')
a_list = []
another_list = ["value1", "value2", "value3"]
print(another_list[0] == "value1")  # True

# get last element with -1
print(another_list[-1])  # value3

# cannot assign that expands list
# another_list[3] == "value4"  # IndexError: list index out of range

# contains use 'in' keyword
print("value2" in another_list)  # True

# length use 'len' keyword
print(len(another_list))  # 3

# remove use 'del' keyword
del another_list[2]


"""
Slice
    [start:*limit*:*step*]
    [<start inclusive>:<stop exclusive>]
    sequence[start:stop] start to stop -1
    sequence[start:] start to end
    sequence[:stop] beginning stop -1
    sequence[start:stop:step] start to stop -1 counting by step
    sequence[:] all elements
    sequence[::] all elements
    sequence[::step] all elements counting by step
"""
print('--> Slice')
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[0:3])
print(fruits[:3])
print(fruits[3:len(fruits)])

x = ['a', 'b', 'c', 'd', 'e']
print(x[2:4])
print(x[4:2:-1])

x[2:4] = ['i', 'j']  # Modifies mutable list in place.
r = x[2:4]  # Creates new list.

print(fruits[::3])  # Prints every third fruit.

# slicing array
# does not modify list, it just skips specified indices
# <index>: to skip from start
# :<index> to skip from end
print("# Slicing array")
a_list.append("1")
a_list.append("2")
a_list.append("3")
print(a_list)  # ['1', '2', '3']
print(a_list[1:])  # ['2', '3']
print(a_list[:-1])  # ['1', '2']
print(a_list[:2])  # ['1', '2']


"""
Append
    Always appends 1 element, regardless if element is a list.
"""
print('--> Append')
x = ['a', 'b', 'c', 'd', 'e']
x.append('f')

more_letters = ['g', 'h']
x.append(more_letters)
print(x)


"""
Extend
    Append multiple items.
"""
print('--> Extend')
x.extend(more_letters)
print(x)


"""
Insert
    Specify item and location.
"""
print('--> Insert')
x.insert(0, 'z')
x.insert(5, 'm')
print(x)


"""
Delete
"""
del x[0]
print(x)


"""
Remove
    Removes first occurrence
"""
x.remove('c')
print(x)

try:
    x.remove('Wombat')
except ValueError as err:
    pass


"""
Pop
"""
print(x.pop(4))


"""
Loop
"""
for value in x:
    print(value)


"""
Tuple
    Fixed size
    Read-only
    Collection of related items
    Supports some sequence operations
    Think 'struct' or 'record'
    Used when you need to pass multiple values to or form a function, but the values are not all the same type
    Use a tuple when you have a collection of related objects, which may or may not be similar
    To specify a one-element tuple use a trailing comma, otherwise it will be interpreted as a single object
        one_element_tuple = 'one',
    Create a tuple with a comma separated list. Parenthesis are only required when the tuple is nested in a larger data structure
"""
print('--> tuple')

hostinfo = ('gemini', 'linux', 'ubuntu', 'hardy', 'Bom Smith')
print(hostinfo)

birthday = ('April', 5, 1978)
print(birthday)

"""
Iterable unpacking
    Copy iterable to list of variables
    Can have one wild card
    Frequently used with list of tuples
    Power of unpacking comes when looping over a sequence of tuples and passing tuples (or other iterables) into a function
"""
print('--> unpacking')

month, day, year = birthday
print(month, day, year)

# List of 3-element tuple
people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

# For loop unpacks each tuple into three variables
for first_name, last_name, org in people:
    print("{} {}".format(first_name, last_name))

# If you have too many vars and get unpacking error you can use *
# e.g. *org or *_ to indicate extra stuff you don't plan on using


"""
Unpacking Function Arguments
    Go from iterable to list of items
    Use * or **
    * used to unpack list or tuple (or similar iterable)
    ** used to unpack dictionary or similar
"""
print('--> unpacking function arguments')

# List of 4-element tuple
people = [
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Rattburger', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]


# Function takes 4 (positional) parameters
def person_record(first_name, last_name, city, state):
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))


# How do we pass single tuple into function that requires 4 parameters?
# Use index, or more Pythonic approach use unpacking

# Person is a tuple (one element of the list)
for person in people:
    # *person unpacks the tuple into four individual parameters
    person_record(*person)


# Another example
BARLEYCORN = 1 / 3.0
CM_TO_INCH = 2.55
MENS_START_SIZE = 12
WOMENS_START_SIZE = 10.5

FMT = '{:6.1f} {:8.2f} {:8.2f}'
HEADFMT = '{:>6s} {:>8s} {:>8s}'

HEADINGS = ['Size', 'Inches', 'CM']

SIZE_RANGE = []
for i in range(6,14):
    SIZE_RANGE.extend([i, i + .5])


def shoe_sizes():
    for heading, flag in [("MEN'S", True), ("WOMEN'S", False)]:
        print(heading)
        # format expects individual arguments for each placeholder;
        # the asterisk unpacks HEADINGS into individual strings
        print((HEADFMT.format(*HEADINGS)))
        for size in SIZE_RANGE:
            inches, cm = get_length(size)
            print(FMT.format(size, inches, cm))

        print()


def get_length(size, mens=True):
    if mens:
        start_size = MENS_START_SIZE
    else:
        start_size = WOMENS_START_SIZE

    inches = start_size - ((start_size - size) * BARLEYCORN)
    cm = inches * CM_TO_INCH
    return inches, cm

shoe_sizes()
