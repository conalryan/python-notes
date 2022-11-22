#!/usr/bin/env python

import threading
import random
import time

"""
Thread Class
    Subclass Thread
    Must call base class's init()
    Must implement run()
    Can implement helper methods
    Syntax
        class SomeClass(threading.Thread):
            pass

    Class that starts a thread, and performs some task. Such a class can be
    repeatedly instantiated, with different parameters, and then started as needed.

    The class can be as elaborate as the business logic requires. There are only two rules:
        1. super().__init__()
            The class must call the base class's init()
            Best way to invoke the base class init() is to use super()
        2. run()
            It must implement a run() method.
            start() method
                The run() method is invoked when you call the start() method on the thread object.
                The start() method does not take any parameters, and thus run() has no parameters as well.

    Other than that, the run() method can do pretty much anything it wants to.
    Any per-thread arguments can be passed into the constructor when the thread object is created.
"""


class SimpleThread(threading.Thread):

    def __init__(self, num):
        # Call base class constructor - REQUIRED
        super().__init__()
        self._threadnum = num

    # The function that does the work in the thread
    def run(self):
        time.sleep(random.randint(1,10))
        print("Hello from thread {} \n".format(self._threadnum))


for i in range(10):
    # Create the thread
    t = SimpleThread(i)
    # Launch the thread
    t.start()

print("Done.")

