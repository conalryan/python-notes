#!/usr/bin/env python

"""
Creating a New XML Document
    Create root element
    Add descendants via SubElement
    Use keyword arguments for attributes • Add text after element created
    Create ElementTree for import/export

    1. root element
        To create a new XML document, first create the root (top-level) element.
        This will be a container for all other elements in the tree.
        If your XML document contains books, for instance, the root document might use the "books" tag.
        It would contain one or more "book" elements, each of which might contain author, title, and ISBN elements.

    2. SubElement
        Once the root element is created, use SubElement to add elements to the root element, and then nested Elements as needed.
        SubElement returns the new element, so you can assign the contents of the tag to the text attribute.

    3. ElementTree
        Once all the elements are in place, you can create an ElementTree object to contain the elements and allow you to write out the XML text. From the ElementTree object, call write.

    ET.tostring()
        To output an XML string from your elements, call ET.tostring(), passing the root of the element tree as a parameter.
        It will return a bytes object (pure ASCII), so use .decode() to convert it to a normal Python string.
"""