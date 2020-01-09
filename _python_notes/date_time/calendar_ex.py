#!/usr/bin/env python

import os
import calendar
import webbrowser

"""
Calendar
    Two classes for generating calendars
        1. TextCalendar:
            formatmonth()
            formatyear()
            prmonth()
            pryear()
        2. HTMLCalendar:
            formatmonth()
            formatyear()
            formatyearpage()
"""

# Text calendar
textcal = calendar.TextCalendar()
print(textcal.formatmonth(2012, 1))

# HTML calendar
htmlcal = calendar.HTMLCalendar()
formatted_month = htmlcal.formatmonth(2012, 1)

html_file_name = 'sample_calendar.html'

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_month)
    webbrowser.open("file://" + os.path.realpath(html_file_name))

