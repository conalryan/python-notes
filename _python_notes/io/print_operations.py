#!/usr/bin/env python

"""
print()
- Normally outpus a newline after its arguments, the can be controlled with the end parameter.
- Puts spaces between its arguments by default. Set the 'sep' parameter to desired separator.
"""
a = 'Apple'
b = 'Banana'
c = 'Cantalope'

print(a, b, c)
# Under the hood it does this
print(str(a), str(b), str(c))

print(a, b, c, sep='/')

print(a, b, c, flush=True)


"""
sys.stderr

"""
import sys

print("Houston we have a problem", file=sys.stderr)