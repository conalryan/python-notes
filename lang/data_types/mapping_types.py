#!/usr/bin/env python

"""
Mapping types:
    - dict
    - set
    - frozenset
"""


"""
Dictionaries
    Mapped set of values indexed by immutable key.
    Key value pairs.
    Similar to JSON.
    Can have nested dictionaries.
    As of 3.6 dictionaries are ordered.
    Keys must be hashable, i.e. immutable. Use strings, numbers, tuples of immutable type.
    
    d = dict()
    d = {}
"""
a_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": 123,
    "a_none_key": None
}

a_list_of_dictionaries = [
    {"key1": "value1"},
    {"dic_2": "the value"}
]

# pass key as index
print(a_dictionary["key2"])  # value2

# careful of key not found error
# print(a_dictionary["key_that_doesnt_exist"])  # KeyError: 'key_that_doesnt_exist'

# use get() with default if key not found
print(a_dictionary.get("key_that_doesnt_exist", "default_value"))  # default_value

# .keys()
print(a_dictionary.keys())

# .values()
print(a_dictionary.values())

# set value
a_dictionary["key1"] = "val has been changed"

# delete key
del a_dictionary["key2"]

print("---------- add, append, dict ----------")
# dealing with adding to dictionary
my_month_dict = {
    "1": {"11": [111]}
}
print(my_month_dict)

# add new key
my_month_dict["2"] = {str(22): [222, 222]}
print(my_month_dict)

# add new month
month = 3
day = 33
value = 333

# get the month or create a new object if not found.
month_in_dict = my_month_dict.get(str(3), {})
# get day in the month or create a new array if not found.
day_in_dict = month_in_dict.get(str(day), [])
day_in_dict.append(value)
# set month
month_in_dict[str(day)] = day_in_dict
# set dict
my_month_dict[str(month)] = month_in_dict

print(my_month_dict)

# add new day
month = 3
day = 34
value = 344

month_in_dict = my_month_dict.get(str(month), {})
day_in_dict = month_in_dict.get(str(day), [])
day_in_dict.append(value)
# set month
month_in_dict[str(day)] = day_in_dict
# set dict
my_month_dict[str(month)] = month_in_dict

print(my_month_dict)

# append value to day
month = 3
day = 34
value = 345

month_in_dict = my_month_dict.get(str(month), {})
day_in_dict = month_in_dict.get(str(day), [])
day_in_dict.append(value)
# set month
month_in_dict[str(day)] = day_in_dict
# set dict
my_month_dict[str(month)] = month_in_dict

print(my_month_dict)


airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}


"""
dict
    dict()
    {}
"""
d1 = dict()
d2 = {}
d3 = dict(EWR='Newark', BOS='Boston')
stuff = [('a', 5), ('m', 9)]
d4 = dict(stuff)
print(d4)


"""
Zip
    Builtin
"""
keys = ['a', 'm', 'b']
values = [5, 9, 6]

d5 = dict(zip(keys, values))


"""
Pretty print
"""
from pprint import pprint

pprint(airports)


"""
Loop
    Key value pair
"""
for k, v in d4.items():
    print(k, v)


"""
get
    Returns value or a default if not found
"""
print(airports.get('ELM', 'not found'))


"""
Update
    Merges a dictionary to another dictionary.
    Source overwrites target
"""
more_airports = {'MAN': 'Manchester, NH'}
airports.update(more_airports)
print(airports)


"""
sorted
"""
for k , v in sorted(airports.items()):
    print(k, v)


""""
setdefault
    Returns value if defined.
    If not defined it adds it to the dict.
"""
print(airports.setdefault('BOS', 'New England'))
print(airports.setdefault('ELM', 'Elmira-Corning'))


"""
Intersection & (e.g. d1 & d2)
Union | (e.g. d1 | d2)
Opposite of intersection ^ (e.g. d1 ^ d2)
Only one - (e.g. d1 - d2)
"""


"""
set
    Similar to dictionary but only contains keys.
    Unique collection of values.
    Two types:
        1. Dynamic is mutable.
        2. frozenset is fixed (immutable), like a tuple.
    Removes duplicates
    
    s = set()
    f = frozenset()
"""
food = ['spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'eggs']

f = set(food)
print(f)