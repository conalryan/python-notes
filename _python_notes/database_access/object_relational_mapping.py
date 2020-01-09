#!/usr/bin/env python

"""
Object-relational Mapping
    No SQL required
    Maps a class to a table
    All DB work is done by manipulating objects
    Most popular Python ORMs
        SQLAlchemy
            Used by Flask
        Django
            Complete Web framework but provides ORM as subpackage

    Object-relational mapper is a module or framework that creates a level of abstraction above the actual database
    tables and SQL queries. A Python class (object) is mapped to the actual table.

    Instead of querying the database, you call a search method on an object representing a table.
    To add a row to the table, you create a new instance of the table class, populate it, and call a method like save().

    2 options
        1. Design the database with the ORM.
            Create class for each table in database.
            Run ORM command which executes the queries needed to build the database
        2. Map tables to an existing database.
            Create classes to match the schemas that have already been defined int eh database.
            SQLAlchemy and Django ORM have tools to automate this process.
"""