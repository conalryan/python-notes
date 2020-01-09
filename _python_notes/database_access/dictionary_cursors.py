#!/usr/bin/env python

import sqlite3
from collections import namedtuple

"""
Dictionary Cursors
    Indexed by column name
    Not standardized in the DB API
    Standard cursor provided by the DB API returns a tuple for each row
    Most DB packages provide other kinds of cursors, including user-defined versions.
    Dictionary cursor is a very common alternative where each row returns a dictionary where keys are column names and values are row values
    For the packages that don't have a dictionary cursor, you can make a generatro function that will emulate one

Python package      How to get a dictionary cursor
---------------------------------------------------------------
pymysql             import pymysql.cursors
                    conn = pymysql.connect(...,
                        cursorclass = pymysql.cursors.DictCursor
                    )
                    dcur = conn.cursor()
                    all cursors will be dict cursors
                    
                    dcur = conn.cursor( pymysql.cursors.DictCursor)
                    only this cursor will be a dict cursor

cx_oracle           Not available

pyodbc              Not available

pgdb                Not available

pymssql             conn = pymssql.connect (..., as_dict=True) dcur = conn.cursor()

psychopg            import psycopg2.extras
                    dcur =
                    conn.cursor(cursor_factory=psycopg.extras.DictCursor)

sqlite3             conn = sqlite3.connect (..., row_factory=sqlite3.Row)
                    dcur = conn.cursor()
                    conn.row_factory = sqlite3.Row
                    dcur = conn.cursor()

"""
s3conn = sqlite3.connect("data/presidents.db")
# uncomment to make _all_ cursors dictionary cursors
# conn.row_factory = sqlite3.Row

NAME_QUERY = '''
    select firstname, lastname
    from presidents
    where termnum < 5
'''

cur = s3conn.cursor() 

# select first name, last name from all presidents
cur.execute(NAME_QUERY)

for row in cur.fetchall():
    print(row)
print('-' * 50)

# Default cursor returns tuple for each row
dcur = s3conn.cursor()

# make _this_ cursor a dictionary cursor
# Row object is tuple/dict hybrid; can be indexed by position OR column name
dcur.row_factory = sqlite3.Row

# select first name, last name from all presidents
dcur.execute(NAME_QUERY)

for row in dcur.fetchall():
    # Selecting by column name
    print(row['firstname'], row['lastname'])

print('-' * 50)


"""
Metadata
    cursor.dictionary
        Returns tuple of tuples
    Fields
        name
        type_code
        display_size
        internal_size
        precision
        scale
        null_ok
    Once a query has been executed, the cursor's description() method returns metadata about the columns in the query as a tuple of tuples
    There is one tuple for each column in teh query; each tuple contains a tuple of 7 values describing the column.
    Example get the names of the columns
        names = [d[0] for d in cursor.description]
    For non-query statements, cursor.description returns None
    Names are based on the query (with possible aliases), and not necessarily on the names in the table.
"""
print('--> metadata')
s3conn = sqlite3.connect("data/presidents.db")

c = s3conn.cursor()


def row_as_dict(cursor):
    """Generate rows as dictionaries"""
    column_names = [desc[0] for desc in cursor.description]
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        yield row_dict


# select first name, last name from all presidents
num_recs = c.execute('''
    select lastname, firstname
    from presidents
''')

for row in row_as_dict(c):
    print(row['firstname'], row['lastname'])


"""
Example of named tuples rather than dictionary for each row
"""
print('--> named tuple')
def NamedTupleCursor(cursor):
    """Generate rows as named tuples"""
    column_names = [desc[0] for desc in cursor.description]
    name_str = ' '.join(column_names)
    # "RowTuple" is an arbitrary name -- any name could be used here
    RowTuple = namedtuple('RowTuple', name_str)

    for row in cursor.fetchall():
        row_tuple = RowTuple(*row)
        yield row_tuple


with sqlite3.connect("data/presidents.db") as s3conn:

    c = s3conn.cursor()

    # select first name, last name from all presidents
    num_recs = c.execute('''
        select firstname, lastname
        from presidents
    ''')

    for row in NamedTupleCursor(c):
        print(row.firstname, row.lastname)
