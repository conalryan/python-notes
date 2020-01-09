#!/usr/bin/env python

# Use builtin lib if lxml not available
# import xml.etree.ElementTree as ET
import lxml.etree as ET

# Read and parse XML file
doc = ET.parse('data/solar.xml')

# Get the root (outermost) element — "solarsystem"
root = doc.getroot()

# Loop over tags; these are just strings; this is not XML-related
for tag in 'inner', 'outer', 'dwarf':

    # Print out tag
    print('{}:'.format(tag.title()))

    # Find the child of the root element whose name is "innerplanets", "outerplanets", etc.,
    section = root.find('{}planets'.format(tag))

    # Loop through the children of that section (which are all "planet" tags)
    for planet in section:

        # For each planet element, get the value of the "planetname" attribute.
        print('\t' + planet.get("planetname"))
