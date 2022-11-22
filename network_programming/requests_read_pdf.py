#!/usr/bin/env python

import sys
import os

import requests

# Target URL
url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'

# Name of PDF file for saving
saved_pdf_file = 'nasa_iss.pdf'

# Open the URL
response = requests.get(url)

# Check status code from the response
if response.status_code == requests.codes.OK:

    # Open local file as write bytes
    with open(saved_pdf_file, 'wb') as pdf_in:
        # Write data to a local file in binary mode; response.content is data from URL
        pdf_in.write(response.content)

    # Select platform and choose the app to open the PDF file
    if sys.platform == 'win32':
        cmd = saved_pdf_file
    elif sys.platform == 'darwin':
        cmd = 'open ' + saved_pdf_file
    else:
        cmd = 'acroread ' + saved_pdf_file

    # Launch the app
    os.system(cmd)
