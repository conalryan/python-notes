#!/usr/bin/env python

"""
Modules
    Files containing Python code
    File name is the module name with the suffix .py appending
    Within a module the module's name (as a string) is available as the value of the global variable name
    No real difference from scripts
    Used to contain functions that can be loaded as needed by scripts.
    Simple module can contain one or more functions
    Complex modules can contain initialization coe as well
    Python classes are also implemented as modules
    Module is only loaded once, even if there are multiple places in an application that import it.
    Modules and packages should be documented with docstrings
    Example
        To use a module named spam.py, say import spam
        Then use the module name to access the functions or other attributes

Import
    import statement loads modules
    3 variations:
        1. import module
            Loads module so its data and functions can be used
            Does not put its attributes (names of classes, functions, and variables) into the current namespace
        2. from module import function-list
            imports only the function(s) specified into the current namespace
            Other functions are not available (even though they are loaded into memory)
        3. from module import * use with caution!
            Loads the module and imports all functions that do not start with an underscore into the current namespace
            Should be used with caution
            It can pollute the current namespace and possibly overwrite builtin attributes or attributes from a different module
    Imported names may overwrite existing names
    Be careful to read the documentation
    Always import the entire module or import names explicitly, never use *
    Any code in a module that is not contained in function or method is executed when the module is imported. Can include data assingments, startup task, connecting to a db, opening a file etc.
    Note
        The first time a module is loaded, the interpreter creates a version compiled for faster loading
        This version has platform information embedded in the name, and has the extension .pyc.
        These .pyc files are put in a folder named _pychache_


Search Path
    Searches
        Current folder
        sys.path (PYTHONPATH)
        Predefined locations
    PYTHONPATH
        Add custom locations by putting one or more directories in PYTHONPATH environment variable
        Separate multiple paths by semicolons for Windows or colons for Unix/Linux
        This will add them to sys.path, after the current folder, but before the predefined locations.
        Paths stored in sys.path
        Windows
            set PYTHONPATH=C:"\Documents and settings\Bob\Python"
        Linux/OS X
            export PYTHONPATCH="/home/bob/python"
        You can also append to sys.path in your scripts, but this can result in non-portable scripts because they will fail if the location of the imported module changes
            import sys
            sys.path.extend("/usr/dev/python/libs", "/home/bob/pylib")
"""