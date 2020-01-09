#!/usr/bin/env python

"""
Decorators
    Classic design pattern
    Built into Python, many decorators are provided by the standard library, such as property() or classmethod()
    Implemented via functions or classes
    Can decorate functions or classes
    Can take parameters (but not required to)
    functools.wraps() preserves function's properties
    @ sign i sused to apply a decorator to a function or class
    Decorator is a component that modifies some other component
    Purpose is typically to add functionality, but there are no restrictions on what decorator can do
    Many decorators register a component with some other component (e.g. @app.route() in Flask maps URL to view function)

Decorator                       Description
--------------------------------------------
@abc.abstractmethod             Indicate abstract method (must be implemented).

@abc.abstractproperty           Indicate abstract property (must be implemented).

@asyncio.coroutine              Mark generator-based coroutine.

@atexit.register                Register function to be executed when interpreter (script) exits.

@classmethod                    Indicate class method (receives class object, not instance object)

@contextlib.contextmanager      Define factory function for with statement context managers (no need to create enter() and exit() methods)

@functools.lru_cache            Wrap a function with a memoizing callable

@functools.singledispatch       Transform function into a single-dispatch generic function.

@functools.total_ordering       Supply all other comparison methods if class defines at least one.

@functools.wraps                Invoke update_wrapper() so decorator’s replacement function keeps original function’s name and other properties.

@property                       Indicate a class property.

@staticmethod                   Indicate static method (passed neither instance nor class object).

@types.coroutine                Transform generator function into a coroutine function.

@unittest.mock.patch            Patch target with a new object. When the function/with statement exits patch is undone.

@unittest.mock.patch.dict       Patch dictionary (or dictionary-like object), then restore to original state after test.

@unittest.mock.patch.multiple   Perform multiple patches in one call.

@unittest.mock.patch.object     Patch object attribute with mock object.

"""