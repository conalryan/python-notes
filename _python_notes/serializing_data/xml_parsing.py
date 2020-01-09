#!/usr/bin/env python

import xml.etree.ElementTree as ET

"""
Parsing XML Document
    Use ElementTree.parse()
    returns an ElementTree object
    Use get... or find... methods on ElementTree object to select element
    getroot()
        To get the root element, use the getroot() method.
"""

doc = ET.parse('data/solar.xml')
root = doc.getroot()