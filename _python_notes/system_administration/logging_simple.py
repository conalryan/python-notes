#!/usr/bin/env python

import logging

"""
Logging
     basicConfig()
        filename
            Specify file name
        level
            Configure the minimum logging level
        Messages added at different levels
        Call methods on logging
            logging.DEBUG, WARN, etc.
    File will continue to grow, and must be manually removed or truncated.
    If file does not exist it will be created

Logging Levels
Level Value     CRITICAL FATAL
-------------------------------
50              ERROR
40 WARN         WARNING
30              INFO
20              DEBUG
10              UNSET
"""
# Setup logging; minimal level is WARN
logging.basicConfig(
    filename='log/simple.log',
    level=logging.WARN,
)

# Message will be output
logging.warning('This is a warning')

# Message will NOT be output (because min level is set higher)
logging.debug('This message is for debugging')

# Message will be output
logging.error('This is an ERROR')
logging.critical('This is ***CRITICAL***')
logging.info('The capital of North Dakota is Bismark')
