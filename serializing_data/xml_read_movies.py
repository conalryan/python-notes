#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

# Read and parse the XML file
movies_doc = ET.parse('data/movies.xml')

# Get the root element (<movies>)
movies = movies_doc.getroot()

# Loop through children of root element
for movie in movies:
    # Get 'name' attribute of movie element
    # Get 'director' attribute of movie element
    print('{} by {}'.format(movie.get('name'), movie.findtext('director'),))
