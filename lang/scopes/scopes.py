#!/usr/bin/env python

"""
Name Resolution (AKA Scope)
    Scope is area where an unqualified (not preceded by a module name) name can be looked up
    Scopes used dynamically
    Four levels of scope
        Local:
            Local names bound within a function
            Within a function all assignments and declarations create local names
            All variables found outside of local scope (that is, outside of the function) are read-only
            Class definitions create local scope
        Nonlocal:
            Local names plus local names of outer function(s) (aka closure)
            Nested functions: Code in function B which is defined inside function A has read-only access to all of A's variables
        Global:
            The current module's global names
            Outside of function local scope is the same as the global scope - the module's namespace.
        Builtin:
            Built-in functions (contents of _builtins_ modules)
    Assignments always go into the innermost scope (starting with local)

Global Statement
    global keyword allows function to modify globals variables.  DO NOT USE IT!
    It's better to pass data into functions as parameters and return data as needed
    Mutable objects such as lists, sets and dictionaries can be modified in-place

Nonlocal Statement
    nonlocal keyword can be used like global to make nonlocal variables in an outer function writable
"""
print('--> scopes')

# Global variable
x = 42


def function_a():
    # Local variable to function_a, and nonlocal to function_b
    y = 5

    def function_b():
        # Local variable
        z = 32
        # Local scope
        print("function_b(): z is", z)
        # Nested (nonlocal) scope
        print("function_b(): y is", y)
        # Global scope
        print("function_b(): x is", x)
        # Builtin scope
        print("function_b(): type(x) is", type(x))

    return function_b


# Calling function_a which returns function_B
f = function_a()
# Calling function_b
f()
