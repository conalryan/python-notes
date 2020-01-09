#!/usr/bin/env python

"""
Database Access


DB API
    Several ways to access DBMSs from Python
        DB API is most popular
        DB API is sort of an "abstract class"
        Many modules for different DBMSs using DB API
        Hides actual DBMS implementation

Database                        Python package
-----------------------------------------------
Firebird (and Interbase)        KInterbasDB

IBM DB2                         PyDB2

Informix                        informixdb

Ingres                          ingmod

Microsoft SQL Server            pymssql

MySQL                           pymysql

ODBC                            pyodbc

Oracle                          cx_oracle

PostgreSQL                      psycopg2

SAP DB (also known as "MaxDB")  sapdbapi

SQLite                          sqlite3

Sybase                          Sybase

Connecting to a Server
    Import appropriate library
    Use connect() to get a database object
    Specify host, database, username, password, or None if not needed
    When finished call the close() method
    Many database modules support the context manager (with statement), and will automatically close the db when the with block is exited
    Example
        import sqlite3
        slconn = sqlite3.connect('web_content')
        import pymysql
        myconn = pymysql.connect (host = "myserver1",
                                 user = "adeveloper",
                                 passwd = "s3cr3t",
                                 db = "web_content")
        #  make queries, etc. here ...
        myconn.close()

Package     Database            Connection
-------------------------------------------
cx_oracle   Oracle              ip = 'localhost'
                                port = 1521
                                SID = 'YOURSIDHERE'
                                dsn_tns = cx_Oracle.makedsn(ip, port, SID)
                                db = cx_Oracle.connect('adeveloper', '$3cr3t', dsn_tns)

psychopg    PostgreSQL          psycopg2.connect ('''
                                    host='localhost'
                                    user='adeveloper'
                                    password='$3cr3t'
                                    dbname='testdb'
                                ''')
                                note: connect() has one (string) parameter, not multiple parameters

pymssql     MS-SQL              pymssql.connect (
                                    host="localhost",
                                    user="adeveloper",
                                    passwd="$3cr3t",
                                    db="testdb",
                                )
                                pymssql.connect (
                                    dsn="DSN",
                                )

pymysql     MySQL               pymysql.connect (
                                    host="localhost",
                                    user="adeveloper",
                                    passwd="$3cr3t",
                                    db="testdb",
                                )

pyodbc      Any ODBC -          pyodbc.connect('''
            compliant DB            DRIVER={SQL Server};
                                    SERVER=localhost;
                                    DATABASE=testdb;
                                    UID=adeveloper;
                                    PWD=$3cr3t
                                ''')
                                pyodbc.connect('DSN=testdsn;PWD=$3cr3t')
                                note: connect() has one (string) parameter, not multiple parameters

sqlite3         SqlLite3        sqlite3.connect('testdb')
                                sqlite3.connect(':memory:')

Creating a Cursor
    Cursor can execute SQL statements
    Multiple cursors available
        Standard cursor
            Returns tuples
        Other cursors
            Returns dictionaries
            Leaves data on server
    Once you have a DB object you can create one or more cursors
    A cursor is an object that can execute SQL code and fetch results
    Default cursor for most packages returns each row as a tuple of values.
    There are different types of cursors that can return data in different formats, or that control whether data is stored on the client or server
    Example
        myconn = pymysqlconnect(
            host="myserver1",
            user="adeveloper",
            passwd="s3cr3t",
            db="web_content"
         )
        mycursor = myconn.cursor()

Executing a Statement
    Executing cursor sends SQL to server
    Data not returned until asked for
    Returns number of lines in result set for queries
    Returns lines affected for other statements
    First argument to execute() method is a string containing the SQL statement to run
    Example
        cursor.execute("select hostname, ostype, user from hostinfo")
        cursor.execute('insert into hostinfo values ("foo", 5, "2.6", "arch", "net", 2055, 3072, "bob", 0)')

Fetching Data
    Use one of the fetch methods from the cursor object
    Syntax
        - rec = cursor.fetchone()
            Returns the next available row from the query results
        - recs = cursor.fetchall()
            Returns a tuple of all rows
        - recs = cursor.fetchmany(n)
            Returns up to n rows.
            This is useful when the query returns a large number of rows.
    Example
        cursor.execute("select color, quest from knights where name = 'Robin'")
        (color, quest) = cursor.fetchone()

        cursor.execute("select color, quest from knights")
        rows = cursor.fetchall()

        cursor.execute("select * from huge_table)
        while True:
            rows = cursor.fetchmany(1000)
            if rows == []:
                break
            for row in rows:
                # process row
"""