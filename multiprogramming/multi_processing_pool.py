#!/usr/bin/env python

import random
from multiprocessing import Pool

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
# Number of processes
POOL_SIZE = 30

with open('data/words.txt') as words_in:
    # Read word file into a list, stripping off \n
    WORDS = [w.strip() for w in words_in]

# Randomize word list
random.shuffle(WORDS)


# Actual task
def my_task(word):
    return word.upper()


if __name__ == '__main__':
    # Create pool of POOL_SIZE
    ppool = Pool(POOL_SIZE)

    # Pass wordlist to pool and get results; map assigns values from input list to processes as needed
    WORD_LIST = ppool.map(my_task, WORDS)

    # Print last 20 words
    print(WORD_LIST[:20])

    print("Processed {} words.".format(len(WORD_LIST)))
