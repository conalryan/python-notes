#!/usr/bin/env python

import sys

"""
Executing Modules as Scripts
    __name__ is current module
        set to __main__ if run as script
            __main__ means you are at the top level of the interpreter and your file is run as a script; it was not loaded as module
        set to module_name if imported
    test with if name == "__main__"
    Module can be run directly or imported
"""

# other imports  (standard library, standard non-library, local)

# constants (AKA global variables)


# main function
# program entry point
# main is not a reserved word, but it is a strong convention
def main(args):
    function1()
    function2()


# other functions
def function1():
    print("hello from function1()")


def function2():
    print("hello from function2()")


# If running as a script
if __name__ == '__main__':
    # Call main() with command line parameters (omitting argv[0] the script itself)
    main(sys.argv[1:])
