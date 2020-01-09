#!/usr/bin/env python

from datetime import date, datetime, timedelta
import time
from dateutil import parser
import os


"""
Python modules for datetime
    Standard library:
        datetime
        time
        calendar
        All of above objects (except timedelta) implement strftime()
        Timezone support is weak in standard library, use dateutil instead
    Non-standard Library:
        dateutil:
            Parse dates from text
            Timezones
        arrow:
            Consolidate all date/time related functions into single module.

Store dates
    date
    datetime
    time
    timedelta:
        Difference between 2 dates, datetimes or times
        Returns days, seconds, microseconds
    integer (epoch time)
    tuple (year, month, day, hour, minute, second, weekday, days since December 31, DST flags)

"""


print('# ====================================== Standard ================================================')
"""
date    
"""
print('--> date()')
d = date.today()  # Today's date
print("date.today():", d)
print("date.day:", d.day)
print("date.month:", d.month)
print("date.year:", d.year)


"""
datetime
"""
print('--> datetime()')
now = datetime.now()  # Today's date and time
print("now.day:", now.day)
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)

# Create datetime object
t1 = datetime(2013, 8, 24, 10, 4, 34)
print("datetime(2007, 8, 24, 10, 4, 34):", t1)


"""
timedelta
"""
print('--> timedelta()')
# date
d1 = date(2007, 6, 13)
d2 = date(2007, 8, 24)
d3 = d1 - d2
print("time delta:", d3)
print("time delta days:", d3.days)

# datetime
d1 = datetime(2007, 6, 13)
d2 = datetime(2007, 8, 24)
d3 = d2 - d1
print("time delta:", d3)
print("time delta days:", d3.days)

# timedelta
interval = timedelta(10)
print("interval:", interval)

# Add time to timedelta
d4 = d2 + interval
d5 = d2 - interval
print("d2 + interval:", d4)
print("d2 - interval:", d5)


"""
strftime()
%a  Locale’s abbreviated weekday name
%A  Locale’s full weekday name
%b  Locale’s abbreviated month name
%B  Locale’s full month name
%c  Locale’s appropriate date and time representation
%d  Day of the month as a decimal number [01,31]
%f  Microsecond as a decimal number [0,999999], zero-padded on the left
%H  Hour (24-hour clock) as a decimal number [00,23]
%I  Hour (12-hour clock) as a decimal number [01,12]
%j  Day of the year as a decimal number [001,366]
%m  Month as a decimal number [01,12]
%M  Minute as a decimal number [00,59]
%p  Locale’s equivalent of either AM or PM.
%S  Second as a decimal number [00,61]  (Range really is 0 to 61; this accounts for leap seconds and the very rare double leap seconds)
%U  Week number (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0
%w  Weekday as a decimal number [0(Sunday),6]
%W  Week number (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0
%x  Locale’s appropriate date representation
%X  Locale’s appropriate time representation
%y  Year without century as a decimal number [00,99]
%Y  Year with century as a decimal number
%z  UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive)
"""
print('--> strftime()')
# Bill Gates's birthday
gates_bd = datetime(1955,10,28, 22, 0, 0)
print(gates_bd)
print(gates_bd.strftime('Bill was born on %B %d, %Y at %I:%M %p'))
print(gates_bd.strftime('BG: %m/%d/%y'))
print(gates_bd.strftime('Mr. Gates was born %d-%b-%Y'))
print(gates_bd.strftime('log entry: %Y-%m-%d'))


"""
strptime()
    time.strptime()
        Returns a time tuple (e.g. get year with tuple[0] or tuple.tm_year
    datetime.strptime()
        Returns new datetime object
"""
print('--> strptime()')
data = (
    ('Jan 1, 1970','%b %d, %Y'),
    ('01/01/70','%m/%d/%y'),
    ('1970-01-01', '%Y-%m-%d'),
    ('Jan 1, 1970 at 3:14 pm', '%b %d, %Y at %I:%M %p'),
)

for date_str, parse_template in data:
    time_tuple = time.strptime(date_str, parse_template)  # <1>
    print(time_tuple)

    parsed_date = datetime.strptime(date_str, parse_template) # <2>
    print(parsed_date)


"""
fromtimestamp()
    datetime.fromtimestamp() to get a datetime object from a timestamp
"""
print('--> fromtimestamp()')
statinfo = os.stat('data/some_file.txt')
ts = statinfo.st_atime  # Returns Unix timestamp
print(ts)
d = datetime.fromtimestamp(ts)
print(d)


"""
localtime()
    time.localtime() to get time tuple from a timestamp
"""
print('--> localtime()')
t = time.localtime(ts)
print(t)


"""
time()
    time.time() returns current time as timestamp
"""
print('--> time()')
t = time.time()
print(t)


"""
timetuple() and mktime()
    Convert to timestamp
    Two steps
        1. Convert date and time to a time tuple with some_date.timetuple()
        2. Call time.mktime()
"""
print('--> timetuple() and mktime()')
d = datetime(1975, 4, 2, 12, 9, 55)
# 1. Convert to time tuple
t = d.timetuple()
print(t)
# 2. Call time.mktime() to convert to timestamp
timestamp = time.mktime(t)
print(timestamp)

today = time.time()  # Epoch time for right now

for ts in 86400, timestamp, today:  # Loop through 3 epoch times (86400, timestamp, today)
    # Convert timestamp to time tuple
    tm = time.localtime(ts)
    print(tm)
    print(tm.tm_year, tm.tm_mon, tm.tm_mday)

    # Convert timestamp to Python datetime
    dt = datetime.fromtimestamp(ts)
    print(dt)
    print(dt.year, dt.month, dt.day)


print('# ====================================== dateutil ================================================')
"""
dateutil
    Will parse most date or date/time string without the need to put together directives as with strptime()
    Returns Python datetime object
"""

date_strings = [
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    '04/01/2015',
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    'Apricot 4, 341',
]

for date_string in date_strings:
    try:
        dt = parser.parse(date_string)
        print(dt)
    except ValueError as err:
        print("Can't parse", date_string)
