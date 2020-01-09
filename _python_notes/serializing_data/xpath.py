#!/usr/bin/env python

"""
Using XPath
    Use simple XPath patterns Works with find* methods
    When a simple tag is specified, the find
    methods only search for subelements of the current element.
    For more flexible searching, the find* methods work with simplified XPath patterns.
    To find all tags named 'spam', for instance, use .//spam.

  .//movie
  presidents/president/name/last

ElementTree XPath Summary
Syntax              Meaning
----------------------------
tag                 Selects all child elements with the given tag. For example, “spam” selects all child elements named “spam”, “spam/egg” selects all grandchildren named “egg” in all child elements named “spam”. You can use universal names (“{url}local”) as tags.

*                   Selects all child elements. For example, “*/egg” selects all grandchildren named “egg”.

.                   Select the current node. This is mostly useful at the beginning of a path, to indicate that it’s a relative path.

//                  Selects all subelements, on all levels beneath the current element (search the entire subtree). For example, “.//egg” selects all “egg” elements in the entire tree.

..                  Selects the parent element.

[@attrib]           Selects all elements that have the given attribute. For example, “.//a[@href]” selects all “a” elements in the tree that has a “href” attribute.

[@attrib=’value’]   Selects all elements for which the given attribute has the given value. For example, “.//div[@class=’sidebar’]” selects all “div” elements in the tree that has the class “sidebar”. In the current release, the value cannot contain quotes.

[tag]               Selects all elements that has a child element named tag. In the current version, only a single tag can be used (i.e. only immediate children are supported).
"""