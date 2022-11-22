#!/usr/bin/env python

import logging

"""
Formatting Log Entries
    Add format-format to basicConfig() parameters
    Format is a string containing directives and (optionally) other text
    Use directives in the form of %(item)type
        %(name)s
    Other text is left as-is
    
Log entry formatting directives
Directive               Description
------------------------------------
%(name)s                Name of the logger (logging channel)

%(levelno)s             Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)

%(levelname)s           Text logging level for the message ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")

%(pathname)s            Full pathname of the source file where the logging call was issued (if available)

%(filename)s            Filename portion of pathname

%(module)s              Module (name portion of filename)

%(lineno)d              Source line number where the logging call was issued (if available)

%(funcName)s            Function name

%(created)f             Time when the LogRecord was created (time.time() return value)

%(asctime)s             Textual time when the LogRecord was created

%(msecs)d               Millisecond portion of the creation time

%(relativeCreated)d     Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded (typically at application startup time)

%(thread)d              Thread ID (if available)

%(threadName)s          Thread name (if available)

%(process)d             Process ID (if available)

%(message)s             The result of record.getMessage(), computed just as the record is emitted
"""
# Set the format for log entries
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filename='log/formatted.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.fatal("this is fatal")
