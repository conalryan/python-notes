#!/usr/bin/env python
import os
import sqlite3
import random

FRUITS = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

# Set name of database
DB_NAME = 'fruitprices.db'

CREATE_TABLE = """
create table fruit (
    name varchar(30),
    price decimal
)
"""  # SQL statement to create table

INSERT = '''
insert into fruit (name, price) values (?, ?)
'''  # Parameterized SQL statement to insert one record


def main():
    """
    Program entry point.

    :return: None
    """
    conn = get_connection()
    create_database(conn)
    populate_database(conn)

    read_database()


def get_connection():
    """
    Get a connection to the PRODUCE database

    :return: SQLite3 connection object.
    """
    if os.path.exists(DB_NAME):
        # Remove existing database if it exists
        os.remove(DB_NAME)

    # Connect to (new) database
    s3conn = sqlite3.connect(DB_NAME)
    return s3conn


def create_database(conn):
    """
    Create the fruit table

    :param conn: The database connection
    :return: None
    """

    # Run SQL to create table
    conn.execute(CREATE_TABLE)


def populate_database(conn):
    """
    Add rows to the fruit table

    :param conn: The database connection
    :return: None
    """

    fruit_data = get_fruit_data()

    # Iterate over list of pairs and add each pair to the database
    conn.executemany(INSERT, fruit_data)

    # Commit the inserts; without this, no data would be saved
    conn.commit()


def get_fruit_data():
    """
    Create iterable of fruit records.

    :return: Generator of name/price tuples.
    """

    # Build list of tuples containing fruit, price paris
    return ((f, round(random.random() * 10 + 5, 2)) for f in FRUITS)


def read_database():
    conn = sqlite3.connect(DB_NAME)
    for name, price in conn.execute('select name, price from fruit'):
        print('{:12s} {:6.2f}'.format(name, price))


if __name__ == '__main__':
    main()
