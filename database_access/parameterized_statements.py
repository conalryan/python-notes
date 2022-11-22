#!/usr/bin/env python

import sqlite3

"""
Parameterized Statements
    More efficient updates
    Use placeholder in query
        Placeholders vary by DB
        Check MODULE.paramstyle
            Types include
                'pyformat' meaning '%s'
                'qmark' meaning '?'
    Pass iterable of parameters
    Prevent SQL injection
    Use cursor.execute() or cursor.executemany()
    For efficiency, you cna iterae over of sequence of input datasets when performing a nonquery SQL statment
    The execute() method takes a query, plus an iterable of values to fill in the placeholders.
    The database manager will only parse the query once, then reuse it for subsequent calls to execute()
    Example
        single_row = ("Smith","John","green"),
        multi_rows= [
            ("Smith","John","green"),
            ("Douglas","Sam","pink"),
            ("Robinson","Alberta","blue"),
        ]
        query = "insert into people (lname,fname,color) values (%s,%s,%s)"
        rows_added = cursor.execute(query, single_row)
        rows_added = cursor.executemany(query, multi_rows)
        
Python package      Placeholder for parameters
-----------------------------------------------
pymysql             %s

cx_oracle           :param_name

pyodbc              ?

pymssql             %d for int, %s for str, etc.

Psychopg            %s or %(param_name)s

sqlite3             ? or :param_name

TIP with the exception of pymssql the same placeholder is used for all column types.
"""
with sqlite3.connect("data/presidents.db") as s3conn:

    s3cursor = s3conn.cursor()

    party_query = '''
    select firstname, lastname
    from presidents
        where party = ?
    '''   # ? is SQLite3 placeholder for SQL statement parameter; different DBMSs use different placeholders

    for party in 'Federalist', 'Whig':
        print(party)
        s3cursor.execute(party_query, (party,))  # Second argument to execute() is iterable of values to fill in placeholders from left to right
        print(s3cursor.fetchall())
        print()

