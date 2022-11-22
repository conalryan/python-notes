#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

# parse XML file
doc = ET.parse('data/solar.xml')

# Find all elements (relative to root element) with tag "planet" under "innerplanets" element
inner_nodes = doc.findall('innerplanets/planet')

# Find all elements with tag "planet" under "outerplanets" element
outer_nodes = doc.findall('outerplanets/planet')

print('Inner:')
# Loop through search results
for planet in inner_nodes:
    # Print "name" attribute of planet element
    print('\t',planet.get("planetname"))

print('Outer:')
for planet in outer_nodes:
    # Print "name" attribute of planet element
    print('\t',planet.get("planetname"))

