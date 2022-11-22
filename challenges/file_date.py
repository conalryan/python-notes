#!/usr/bin/env python

import sys, os
from datetime import datetime
import time

"""
Accept one or more file names on the command line, and prints out each file name with
its date of last modification in the format 'Mar 12, 2013'.
"""

for arg in sys.argv[1:]:
    print(arg)
    mtime = os.path.getmtime(arg)  # timestamp

    # Convert timestamp to Python datetime
    dt = datetime.fromtimestamp(mtime)
    print(arg, dt.strftime('%b %d, %Y'))
