#!/usr/bin/env python

import logging

"""
Logging Exception Information
    Use logging.exception()
    Adds exception info to message
    Should only be called in except blocks
"""
# Configure logging
logging.basicConfig(
    filename='log/exception.log',
    level=logging.WARNING,
)

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError:
        # Minimum level
        logging.exception('Logging with exception info')
