#!/usr/bin/env python

# See multiporcessing.dummy.Pool for the easier way
import threading
import random
import time

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

MAX_SLEEP_TIME = 3

# The threads will append words to this list
WORD_LIST = []

# Generic locks
WORD_LIST_LOCK = threading.Lock()
STDOUT_LOCK = threading.Lock()


class SimpleThread(threading.Thread):

    # Thread constructor
    def __init__(self, num, word):
        # Be sure to call parent constructor
        super().__init__()
        self._word = word
        self._num = num

    # Function invoked by each thread
    def run(self):
        time.sleep(random.randint(1, MAX_SLEEP_TIME))

        # Acquire lock and auto release (using the with statement) when finished
        with STDOUT_LOCK:
            print("Hello from thread {} ({})\n".format(self._num, self._word))

        # Acquire lock and auto release (using the with statement) when finished
        with WORD_LIST_LOCK:
            WORD_LIST.append(self._word.upper())


# Make list ("pool") of threads (but see threads_pool.py)
all_threads = []
for i, word in enumerate(WORDS, 1):
    # Create thread
    t = SimpleThread(i, word)

    # Add thread to the "pool"
    all_threads.append(t)

    # Launch the thread
    t.start()

print("All threads launched...")

for t in all_threads:
    # Wait for thread to launch
    t.join()

print(WORD_LIST)
