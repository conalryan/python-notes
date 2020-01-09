#!/usr/bin/env python

"""
Serializing XML
    SAX (Simple API for XML)
        One scan through file processes file as a single strem
        Good for large files
        Uses callbacks on XML parsing events
        Attaches callback functions to SAX events.
        Events are created when the XML reader encounters all the various components of an XML file - begin tags, end tags, data, etc.
    DOM
        Builds a document tree that fully resides in memory
        Python supports both through many libraries
        A top-level Document instance is the root of the tree, and has a single child which is the top-level Element instance
        Element
            Has child nodes representing the content and any sub-elements, which may in turn have further children and so forth.
        Classes
            Text
            Comment
            CDATASection
            EntityReference
            Provide access to XML structure and data.
        Nodes
            Have methods for accessing the parent and child nodes, accessing element and attribute values, i
            insert and delete nodes, and converting the tree back into XML.

    xml.etree.ElementTree
        Is fast, provides both SAX and DOM style parsing, and unlike many of the other modules, has a Pythonic interface.

    lxml.etree
        If available, use lxml.etree, which is a superset of ElementTree with some nice extra features, such as pretty-printing.

XML Modules in the Python 3 Standard Library
Module                  Description
------------------------------------
xml.parsers.expat       Fast XML parsing using Expat

xml.dom                 The Document Object Model API

xml.dom.minidom         Lightweight DOM implementation

xml.dom.pulldom         Support for building partial DOM trees

xml.sax                 Support for SAX2 parsers

xml.sax.handler         Base classes for SAX handlers

xml.sax.saxutils        SAX Utilities

xml.sax.xmlreader       Interface for XML parsers

xml.etree.ElementTree   Pythonic interface to XML

Elements
    Element has ◦ Tag name
    Attributes (implemented as a dictionary)
    Text
    Tail
    Child elements (implemented as a list) (if any)
    SubElement creates child of Element

    When creating a new Element, you can initialize it with the tag name and any attributes.
    Once created, you can add the text that will be contained within the element’s tags, or add other attributes.

    When you are ready to save the XML into a file, initialize an ElementTree with the root element.

    Element class
        The Element class is a hybrid of list and dictionary.
        You access child elements by treating it as a list.
        You access attributes by treating it as a dictionary. (But you can’t use subscripts for the attributes – you must use the get() method).

        Properties
            The Element object also has several useful properties:
            tag
                Element’s tag;
            text
                Text contained inside the element
            tail
                Any text following the element, before the next element.

    SubElement class
        The SubElement class is a convenient way to add children to an existing Element.

    TIP Only the tag property of an Element is required; other properties are optional.

Element properties and methods
Property                    Description
-----------------------------------------
append(element)             Add a subelement element to end of subelements

attrib                      Dictionary of element’s attributes

clear()                     Remove all subelements

find(path)                  Find first subelement matching path

findall(path)               Find all subelements matching path

findtext(path)              Shortcut for find(path).text

get(attr)                   Get an attribute; Shortcut for attrib.get()

getiterator()               Returns an iterator over all descendants

getiterator(path)           Returns an iterator over all descendants matching path

insert(pos,element)         Insert subelement element at position pos

items()                     Get all attribute values; Shortcut for attrib.items()

keys()                      Get all attribute names; Shortcut for attrib.keys()

remove(element)             Remove subelement element

set(attrib,value)           Set an attribute value; shortcut for attr[attrib] = value

tag                         The element’s tag

tail                        Text following the element

text                        Text contained within the element

find(path)                  Finds the first toplevel element with given tag; shortcut for getroot().find(path).

findall(path)               Finds all toplevel elements with the given tag; shortcut for getroot().findall(path).

findtext(path)              Finds element text for first toplevel element with given tag; shortcut for getroot().findtext(path).

getiterator(path)           Returns an iterator over all descendants of root node matching path. (All nodes if path not specified)

getroot()                   Return the root node of the document

parse(filename) parse(fileobj)  Parse an XML source (filename or file-like object)

write(filename,encoding)        Writes XML document to filename, using encoding (Default us- ascii).

Navigating XML Document
    Element is iterable of it children
    find()
        To find the first child element with a given tag, use find('tag').
        This will return the first matching element.
    findall()
        To get all child elements with a given tag, use the findall('tag') method, which returns a list of elements.
    findtext()
        Retrieves text from element
        The findtext('tag') method is the same, but returns the text within the tag.
    Check if a node was found, say
        if node is None:
    but to check for existence of child elements, say
        if len(node) > 0:
    A node with no children tests as false because it is an empty list, but it is not None.
    Tip
        The ElementTree object also supports the find() and findall() methods of the Element object, searching from the root object.

"""