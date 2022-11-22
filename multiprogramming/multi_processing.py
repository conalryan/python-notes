#!/usr/bin/env python

import random
from multiprocessing import Manager, Lock, Process, Queue, freeze_support
from queue import Empty
import time

"""
Multiprocessing Module
    Drop-in replacement for the threading module
        multiprocessing.Process object for threading.Thread object.
        Both use run() as overridable method that does the work.
        Both use start() to launch.
    Uses processed rather than threads to spread out the work.
    Doesn't suffer from GIL issues
    Provides interprocess communication
    Provides process (and thread) pooling
    Solves GIL issue, but the trade-off is that it's slightly more complicated for tasks (processes) to communicate.
    Syntax
        def myfunc(filename):
            pass

        p = Process(target=myfunc, args=('/tmp/info.data',))
    Manager class
        Allows you to create shared variables, as well as locks for them, which work across processes.
        Note: On windows, processes must be starte in the "if __name__ == __main__" block or they will not work.

Global Interpreter Lock (GIL)
    https://wiki.python.org/moin/GlobalInterpreterLock
    In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects.
    It prevents multiple threads from executing Python bytecodes at once.
    This lock is necessary mainly because CPython's memory management is not thread-safe.
    However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.

    The GIL is controversial because it prevents multithreaded CPython programs from taking full advantage of
    multiprocessor systems in certain situations. Note that potentially blocking or long-running operations,
    such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in
    multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL
    becomes a bottleneck.
"""

# Set some constants
NUM_ITEMS = 25000
POOL_SIZE = 100


# Callable class to provide random words
class RandomWord(object):

    def __init__(self):
        with open('data/words.txt') as WORDS:
            self._words = [word.rstrip('\n\r') for word in WORDS]
        self._num_words = len(self._words)

    # __call__(self)
    # Useful for classes that have only one method.
    # Call an instance of the class
    #     r = RandomWord()
    #     r()
    # Instead of
    #     r = RandomWord()
    #     r.some_method()
    def __call__(self):
        return self._words[random.randrange(0, self._num_words)]


# Worker class - inherits from Process
class Worker(Process):

    # Initialize worker process
    def __init__(self, name, q, result_lock, result):
        Process.__init__(self)
        self.q = q
        self.result = result
        self.result_lock = result_lock
        self.name = name

    # Will be called when process starts
    def run(self):
        while True:
            try:
                # Get data form the queue
                s1 = self.q.get(block=False)

                # Modify data
                s2 = s1.upper()

                with self.result_lock:
                    # Add to shared result
                    self.result.append(s2)

            # Quit when there is no more data in the queue
            except Empty:
                break


if __name__ == '__main__':
    # Create empty Queue object
    q = Queue()

    # Create manager for shared data
    manager = Manager()

    # Create list-like object to be shared across all processes
    shared_result = manager.list()

    # Create locks
    result_lock = Lock()

    # Create callable RandomWord instance
    random_word = RandomWord()
    for i in range(NUM_ITEMS):
        w = random_word() # invokes __call__ on RandWord instance
        # Fill the queue
        q.put(w)

    start_time = time.ctime()

    # Create empty list to hold processes
    pool = []
    # Populate the process pool
    for i in range(POOL_SIZE):
        name = "Worker {:03d}".format(i)

        # Create worker process
        w = Worker(name, q, result_lock, shared_result)

        # Actually start the process. Note: Windows, should only call x.start() from main() and may not work inside IDE
        w.start()

        # Add to process pool
        pool.append(w)

    for t in pool:
        # Wait for thread to finish
        t.join()

    end_time = time.ctime()

    print((shared_result[-50:]))  # print last 50 entries in shared result
    print(len(shared_result))
    print(start_time)
    print(end_time)
