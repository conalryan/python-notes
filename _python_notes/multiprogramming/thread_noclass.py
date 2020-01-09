#!/usr/bin/env python

import threading
import random
import time

"""
Threads for the impatient
    No class needed (created "behind the scenes")
    For simple applications
    For many threading tasks, all you need is a run() method and maybe some arguemtns to pass to it.
    For simple tasks, you can just create an instance of Thread, passing in positional or keyword arguments
    Syntax
        threading.Thread(target=<some_function>, args=(<some_args,))
"""


# Function to launch in each thread
def doit(num):
    time.sleep(random.randint(1,10))
    print("Hello from thread {}".format(num))


for i in range(10):
    # Create thread
    t = threading.Thread(target=doit,args=(i,))
    # Launch thread
    t.start()
