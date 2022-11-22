#!/usr/bin/env python

import sys
import os
from urllib.request import urlopen
from urllib.error import HTTPError

# url to download a PDF file of a NASA ISS brochure
# Target URL
url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'

# Name of PDF file for saving
saved_pdf_file = 'nasa_iss.pdf'

try:
    # Open the URL
    URL = urlopen(url)
except HTTPError as e:  # Catch any HTTP errors
    print("Unable to open URL:", e)
    sys.exit(1)

# Read all data from URL, in binary mode
pdf_contents = URL.read()
URL.close()
    
with open(saved_pdf_file, 'wb') as pdf_in:
    # Write data to a local file in binary mode
    pdf_in.write(pdf_contents)

# Select platform and choose the app to open the PDF file
if sys.platform == 'win32':
    cmd = saved_pdf_file
elif sys.platform == 'darwin':
    cmd = 'open ' + saved_pdf_file
else:
    cmd = 'acroread ' + saved_pdf_file

# Launch the app
os.system(cmd)
