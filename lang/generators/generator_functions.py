#!/usr/bin/env python

"""
Generator Functions
    Mostly like a normal function
    Use yield rather than return
    Maintains state between calls, unlike a normal function.
    Each time yield statement is reached, it provides the next value in the sequence.
    When there are no more values, the function calls return, and the loop stops.
"""
print('--> generator functions')


# Silly generator function
def silly():
    yield 'spam'
    yield 'ham'
    yield 'eggs'


s = silly()

print(s)  # <generator object silly at 0x1038b9990>
print(type(s))  # <class 'generator'>

for thing in s:
    print(thing)  # spam ham eggs


# Next prime generator
def next_prime(limit):
    # Initialize flags. Create an array with every value as False up to limit + 1
    flags = [False] * (limit + 1)

    for i in range(2, limit):
        if flags[i]:
            continue
        for j in range(2 * i, limit + 1, i):
            flags[j] = True
        # Execution stops here until next value is requested by for-in loop
        yield i


# nex_prime returns a generator object
for p in next_prime(200):
    print(p, end=' ')


# Trim generator
def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            if line.endswith('\n'):
                line = line.rstrip('\n\r')
            # yield causes this function to return a generator object
            yield line


# Looping over the generator object returned by trimmed()
for line in trimmed('data/mary.txt'):
    print(line)