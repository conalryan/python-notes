#!/usr/bin/env python

import queue
from threading import Thread,Lock as tlock
import time
import random

"""
Using Queues
    Queue contains a list of objects
    Sequence is FIFO
    Worker threads can pull items form the queue
    Queue structure has builtin locks
    
    Threaded applications often have some sort of work queue data structure.
    When thread becomes free, it will pick up work to do from the queue.
    When a thread creates a task, it will add that task to the queue.
    
    Queue must be guarded with locks. Python provides the Queue module to take care of all
    the lock creation, locking and unlocking, and so on, so that you don't have to bother with it.
"""
NUM_ITEMS = 25000
POOL_SIZE = 100

# Initialize empty queue
q = queue.Queue(0)

shared_list = []

# Create locks
shared_list_lock = tlock()
stdout_lock = tlock()


# Define callable class to generate words
class RandomWord(object):

    def __init__(self):
        with open('data/words.txt') as WORDS:
            self._words = [word.rstrip('\n\r') for word in WORDS.readlines()]
        self._num_words = len(self._words)
        
    def __call__(self):
        return self._words[random.randrange(0, self._num_words)]


# Worker thread
class Worker(Thread):

    # Function invoked by thread
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    # Function invoked by thread
    def run(self):
        while True:
            try:
                # Get next item from thread
                s1 = q.get(block=False)
                s2 = s1.upper() + '-' + s1.upper()

                # Acquire lock, then release when done
                with shared_list_lock:
                    shared_list.append(s2)

            # When queue is empty, it raises Empty exception
            except queue.Empty:
                break


# Fill the queue
random_word = RandomWord()
for i in range(NUM_ITEMS):
    w = random_word()
    q.put(w)

start_time = time.ctime()

# Populate the threadpool
pool = []
for i in range(POOL_SIZE):
    name = "Worker {:c}".format(i+65)

    # Add thread to pool
    w = Worker(name)

    # Launch the thread
    w.start()

    # Add thread to the pool
    pool.append(w)
    
for t in pool:
    # Wait for thread to finish
    t.join()

end_time = time.ctime()

print(shared_list[:20])

print(start_time)
print(end_time)

