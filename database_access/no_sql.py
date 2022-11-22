#!/usr/bin/env python

import re
from pymongo import MongoClient

"""
NoSQL
    Non-relational database
    Document-oriented
    Can be hierarchical (nested)
    Examples
        MongoDB
        Cassandra
        Redis

    Database consists of documents which are indexed and may contain nested data.
    NoSQL databases don't contain tables and don't have relations.

    Relational databases are great for tabular data.  They are not good for nested data.

    Complex structures that suite NoSQL
        Geo-spatial
        Engineering diagrams
        Molecular modeling

    NoSQL can adapt to changing data structures without having to rebuild tables if columns are added, deleted or modified.
"""

# MongoDB Example:

FIELD_NAMES = (
    'termnumber lastname firstname '
    'birthdate '
    'deathdate birthplace birthstate '
    'termstartdate '
    'termenddate '
    'party'
).split()  # Define some field name

# Get a Mongo client
mc = MongoClient()

try:
    # Delete 'presidents' database if it exists
    mc.drop_database("presidents")
except:
    pass

# Create new database named 'presidents'
db = mc["presidents"]

# Get the collection from presidents db
coll = db.presidents

# Open a data file
with open('data/presidents.txt') as PRES:
    for line in PRES:
        flds = line[:-1].split(':')
        kvpairs = zip(FIELD_NAMES, flds)
        record_dict = dict(kvpairs)
        # Insert a record into the collection
        coll.insert(record_dict)

# Get list of collections
print(db.collection_names())
print()

# Search collection for doc where termnumber == 16
abe = coll.find_one({'termnumber': '16'})
for field in FIELD_NAMES:
    # Print all fields for one record
    print("{0:15s} {1}".format(field.upper(), abe[field]))

print('-' * 50)

# Loop through all records in collection
for president in coll.find():
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

# Find record using regular expression
rx_lastname = re.compile('^roo', re.IGNORECASE)
for president in coll.find({'lastname': rx_lastname}):
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

# Find record searching multiple fields
for president in coll.find({"birthstate": 'Virginia', 'party': 'Whig'}):
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))

print('-' * 50)
print("removing Millard Fillmore")
# Delete record
result = coll.remove({'lastname': 'Fillmore'})
print(result)
# Delete record
result = coll.remove({'lastname': 'Roosevelt'})
print(result)
print('-' * 50)
# Get count of records
result = coll.count()
print(result)
