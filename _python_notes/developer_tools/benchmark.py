#!/usr/bin/env python

import timeit

"""
Benchmarking
    Use the timeit module to benchmark two or more code snippets.
    Create a timer object with specified # of repetitions
"""
# Setup coe is only executed once
setup_code = 'values = []'

test_code_one = '''
for i in range(10000):
    values.append(i)
'''  # Code fragment executed many times

test_code_two = ''' 
i = 0
while i < 10000:
    values.append(i)
    i += 1
'''  # Code fragment executed many times

# Timer object creates time-able-code
t1 = timeit.Timer(test_code_one, setup_code)
t2 = timeit.Timer(test_code_two, setup_code)

print("test one:")
# timeit() runs code fragment N times
print(t1.timeit(1000))
print()

print("test two:")
# timeit() runs code fragment N times
print(t2.timeit(1000))
print()