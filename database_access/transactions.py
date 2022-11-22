#!/usr/bin/env python

"""
Transactions
    Allow safer control of updates
    commit() to save transactions
    rollback() to discard
    Default is autocommit off
    autocommit\=True to turn on

    Sometimes a database task involves more than one change to your database (i.e. more than one SQL statement).
    You don't want the first SQL statement to succeed and the second to fail; this would leave your database in a corrupt state.

    Transactions allow you to make multiple changes to your database and only commit the changes if all the SQL statemenets were successful.
    All Python DB API packages start a transaction when a connection is made. At this point you can call
    CONNECTION.commit() or CONNECTION.rollback(). For most packages if you don't call commit() after modify a table, the data will not be saved.

    Example
        try:
            for info in list_of_tuples:
               cursor.execute(query,info)
        except SQLError:
            dbconn.rollback()
        else:
            dbconn.commit()

    Note pymysql only supports transaction processing when using the InnoDB engine.
"""