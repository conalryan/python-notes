#!/usr/bin/env python

# Python style
• Code is read more often than it is written!
• Style guides enforce consistency and readability
• Indent 4 spaces (do not use tabs)
• Keep lines ⇐ 79 characters
• Imports at top of script, and on separate lines
• Surround operators with space
• Comment thoroughly to explain why and how code works when not obvious
• Use docstrings to explain how to use modules, classes, methods, and functions
• Use lower_case_with_underscores for functions, methods, and attributes
• Use UPPER_CASE_WITH_UNDERSCORES for globals
• Use StudlyCaps (mixed-case) for class names
• Use _leading_underscore for internal (non-API) attributes

Guido van Rossum, Python’s BDFL (Benevolent Dictator For Life), once said that code is read much more often than it is written.
This means that once code is written, it may be read by the original developer, users, subsequent developers who inherit your code.
Do them a favor and make your code readable. This in turn makes your code more maintainable.
To make your code readable, it is import to write your code in a consistent manner.
There are several Python style guides available, including PEP (Python Enhancement Proposal) 8, Style Guide for Python Code, and PEP 257, Docstring Conventions.
If you are part of a development team, it is a good practice to put together a style guide for the team.
The team will save time not having to figure out each other’s style.

# Program Structure
- All imports at top.
- Modules must be imported before their contents may be accessed.
- Variables, functions, and classes must be declared before use.
- Main function goes at top.
- Main function called at bottom.

Order:
1. import statements
2. global variables
3. main function
4. functions
5. call to main function

Reference:
    script_template
