#!/usr/bin/env python

"""
ElementTree
    Import xml.etree.ElementTree (or lxml.etree) as ET for convenience
    Parse XML or create empty ElementTree
    ElementTree is part of the Python standard library
    lxml is included with the Anaconda distribution.
    Alias
        Since putting "xml.etree.ElementTree" in front of its methods requires a lot of extra typing,
        it is typical to alias xml.etree.ElementTree to just ET when importing it:
            import xml.etree.ElementTree as ET
    Version
        You can check the version of ElementTree via the VERSION attribute:
            import xml.etree.ElementTree as ET
            print(ET.VERSION)

    ElementTree contains root Element
    Document is tree of Elements

    In ElementTree, an XML document consists of a nested tree of Element objects.
    Each Element corresponds to an XML tag.
    An ElementTree object serves as a wrapper for reading or writing the XML text.

    ElementTree.parse()
        If you are parsing existing XML, use ElementTree.parse()
        Creates the ElementTree wrapper and the tree of Elements.
        You can then navigate to, or search for, Elements within the tree.
        You can also insert and delete new elements.

    If you are creating a new document from scratch, create a top-level (AKA "root") element, then create child elements as needed.
        element = root.find('sometag')
        for subelement in element:
            print(subelement.tag)
        print(element.get('someattribute'))
"""