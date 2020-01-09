#!/usr/bin/env python

"""
Pools
    Provided by multiprocessing
    Both thread and process pools
    Simplifies multiprogramming tasks
    Processes a list (or other iterable) of data and do something with the results.
    Object creates a pool of n processes.
    .map()  
        Call .map() method with a function that will do the work, and an iterable of data.
        Returns a list the same size as the list that was passed in.
        Returned list contains the results returned by the function for each item in the original list.
    For a thread pool, import Pool from multiprocessing.dummy. It works exactly the smae, but creates threads.
"""
