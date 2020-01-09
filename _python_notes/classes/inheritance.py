#!/usr/bin/env python

"""
Inheritance
    Specify base class in class definition
    Call base class constructor explicitly
    One or more base classes can be specified as part of the class definition
    Default base class is object
    Base class must already be imported
    Classes may override methods of their base classes (for Java and C++ programmers: all methods in Python are effectively virutal)
    To extend rather than simply replace a base class method, call the base class method directly: BaseClassName.methodname(self, args)
    Super
        You can also use super() function which stands in for the base class
        class Foo(Bar):
            def __init(self):
                super().__init__()  # same as Bar.__init__(self)
        The advantage of super() is that you don't have to specify the base class explicitly, so if you change the base class, it automatically does the right thing
        Follows MRO (method resolution order) to find function
        Great for single inheritance tree
        Use explicit base class names for multiple inheritance
        Syntax
            super().method()
        Use in a class to invoke methods in base classes
        Searches the base classes and their bases, recursively, from left to right until the method is found
        If classes have a diamond shaped inheritance tree, super() may not do what you expect, in that case use the base class name explicitly

"""
class Base(object):

    def some_method(self):
        print('--> Base.some_method()')


class Inheritance(Base):

    def another_method(self):
        print('--> Inhertianc.another_method()')


class OverrideBase(Base):

    def some_method(self):
        super().some_method()
        print('--> OverrideBase.some_method()')


i = Inheritance()
i.some_method()
i.another_method()

o = OverrideBase()
o.some_method()