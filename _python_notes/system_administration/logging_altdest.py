#!/usr/bin/env python

import sys
import logging
import logging.handlers

"""
Logging to Other Destinations
    Use specialized handlers to write to other destinations
    Multiple handlers can be added to one logger
        NTEventLogHandler for Windows event log
        SysLogHandler for syslog
        SMTPHandler for logging via email
        Each can have its own destination and level
    Note
        On Windows, you must run the example script (logging.altdest.py) as administrator. 
        You can find Command Prompt (admin) on the main Windows 8/10 menu. 
        You can also right-click on Command Prompt from the Windows 7 menu and choose "Run as administrator".
"""
# Get logger for application
logger = logging.getLogger('ThisApplication')

# Minimum log level
logger.setLevel(logging.DEBUG)

if sys.platform == 'win32':
    # Create NT event log handler
    eventlog_handler = logging.handlers.NTEventLogHandler("Python Log Test")

    # Install NT event handler
    logger.addHandler(eventlog_handler)
else:
    # Create syslog handler
    syslog_handler = logging.handlers.SysLogHandler()

    # Install syslog handler
    logger.addHandler(syslog_handler)

# Create email handler
# note -- use your own SMTP server...
email_handler = logging.handlers.SMTPHandler(
    ('smtpcorp.com' ,8025),
    'LOGGER@pythonclass.com',
    ['jstrick@mindspring.com'],
    'ThisApplication Log Entry',
    ('jstrickpython', 'python(monty)'),
)

# Install email handler
logger.addHandler(email_handler)

# Goes to all handlers
logger.debug('this is debug')
logger.critical('this is critical')
logger.warning('this is a warning')
