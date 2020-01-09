#!/usr/bin/env python

"""
Developer Tools
    Run pylint to check source code
    Debug scripts
    Find speed bottlenecks in code
    Compare algorithms to see which is faster

Comments
    Keep comments up-to-date
    Use complete sentences
    Block comments describe a section of code
    Inline comments describe a line
    Don't stat the obvious
    Comments that contradict the code are worse than no comments
    Always make a priority of keeping the comments up-to-date when the code changes!
    If a comment is short the period at the end of the sentence can be ommited.
    Use two spaces after a sentence ending period.
    Inline comments are unnecessary and in fact distracint if they stat the obvious.
    Don't do this: x = x + 1  # Increment X
    Only use inline comment if the reason for the statement is not obvious:
        x = x + 1  # Compensate for border

Pylint
    Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for
        some code smells (as defined in Martin Fowler's Refactoring book)
    Developed by Logilab http://www.logilab.fr
    Checks many aspects of code
    Finds mistakes
    Rates your code for standards compliance
    Don't worry if your code has a lower rating!
    Can be highly customized
    Note
        Other tools for analyzing Python code: pyflakes, pychecker
    Customizing
        Run pylint --generate-rcfile
        Redirect to file
        Edit as needed
        Knowledge of regular expressions useful
        Linux/Unix/OS X
            /etc/pylintrc and ~/.pylintrc will be automatically loaded in that order
        Use -rcfile file to specify custom file on Windows

Pyreverse
    Source analyzer
    Reverse engineers Python code
    Part of pylint
    Generates UML diagrams
    Example
        pyreverse -o png -p MyProject -A animal.py mamal.py insect.py

Python Debugger
    Implemented via pdb module
    Supports breakpoints and single stepping
    Based on gbd
    Most IDEs have built-in debugger, it is good to know hwo to debug from the command line.
        python -mpdb script_to_be_debugged.py
    Syntax
        python -m pdb script
    or
        import pdb
        pdb.run('function')
    pdb is usually invoked as a script to debug other scripts
        python -m pdb myscript.py
    Typical usage to run a program under control of the debugger is:
        >>> import pdb
        >>> import some_module
        >>> pdb.run('some_module.function_to_text()')
        > <string>(0)?()
        (Pdb) c    # (c)ontinue
        > <string>(1)?()
        (Pdb) c    # (c)ontinue
        NameError: 'spam'
        > <string>(1)?()
        (Pdb)
    To get help, type h at the debugger prompt.

Stepping through a program
    s single-step, stepping into functions
    n single-step, stepping over functions
    r return from function
    c run to next breakpoint or end
    Pressing Enter repeats most commands; if the previous command was list, the debugger lists the next set of lines

Setting Breakpoints
    b list all breakpoints
    b linenumber (, condition)
    b file:linenumber (, condition)
    b function name (, condition)
    tbreak command creates a one-time breakpoint that is deleted after it is hit the fist time.

Profiling
    Use the profile module from the command line
    Shows where program spends the most time
    Helps find bottlenecks
    Output can be tweaked via options
    Syntax
        python -m profile scriptname.py
    This will output a simple report to STDOUT.
    Specify an output file with -o option.
    Specify sort order with -s option.
    pycallgraph module
        Not in the standard library
        Create a graphical TIP representation of an application’s profile, indicating visually where the application is spending the most time.
"""