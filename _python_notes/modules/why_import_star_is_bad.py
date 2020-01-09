#!/usr/bin/env python

# Imports amps(), voltage(), current() from electrical
from electrical import *
# Imports current() from navigation
from navigation import *


print(current())  # slow (uses navigation.current() because it was imported last)
print(voltage())  # 110
print(amps())  # 10
