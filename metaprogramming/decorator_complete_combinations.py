#!/usr/bin/env python

from functools import wraps, update_wrapper

"""
Decorator Combinations
    There are many combinations of decorators (8 total, to be exact)

function decorators:
    1. function without params
        decorator returns replacement
    2. function with params
        decorator returns wrapper
        wrapper returns replacement
    3. class without params
        __call__ IS replacement
    4. class with params
        __call__ RETURNS replacement

class decorators:
    5. function without params
        __call__ IS replacement
    6. function with params
    7. class without params
    8. class with params
"""


def func_deco_func(wrapped_function):
    """
    function without params decorating a function -- the simplest case

    @func_deco_func
    def bar():
        pass

    same as
    bar = func_deco_func(bar)


    :param wrapped_function: function to decorate
    :return: replacement function
    """

    @wraps(wrapped_function)
    def _replacement(*args, **kwargs):
        print("GREETINGS from func_deco_func!")
        result = wrapped_function(*args, **kwargs)
        return result + 1

    return _replacement


def func_deco_func_param(value=None):
    """
    function with params decorating a function

    @func_deco_func_param('blah')
    def bar():
        pass

    same as
    bar = func_deco_func_param('blah')(bar)
    or,
    wrapper = foo('blah')
    bar = wrapper(bar)


    :param value: decorator parameter
    :return: replacement function
    """

    def wrapper(wrapped_function):

        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from func_deco_func_param -- value is {}!".format(value)))
            result = wrapped_function(*args, **kwargs)
            return result + 2

        return _replacement

    return wrapper


class class_deco_func(object):
    """
    class without params decorating a function

    __call__() is the replacement function

    @class_deco_func
    def bar():
        pass

    same as
    bar = class_deco_func(bar)


    """
    def __init__(self, wrapped_function):
        self.__name__ = wrapped_function.__name__
        self._wrapped = wrapped_function

    def __call__(self, *args, **kwargs):
        print("GREETINGS from class_deco_func!")
        result = self._wrapped(*args, **kwargs)
        return result + 3


class class_deco_func_param(object):
    """
    class with params decorating a function

    __call__() RETURNS the replacement function


    @class_deco_func_param('blah')
    def bar():
        pass

    same as
    bar = class_deco_func_param('blah')(bar)
    or,
    wrapper = class_deco_func_param('blah')
    bar = wrapper(bar)
    """

    def __init__(self, value):
        self._value = value

    def __call__(self, wrapped_function):

        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from class_deco_func_param -- value is {}!".format(self._value)))
            result = wrapped_function(*args, **kwargs)
            return result + 4

        return _replacement


print("Function decorators:")
@func_deco_func
@func_deco_func_param('APPLE')
@class_deco_func
@class_deco_func_param('BANANA')
def target_function(color, value):
    print(("Hello from target_function -- color is {} and value is {}".format(color, value)))
    print(("Target function's name is", target_function.__name__))
    return 10 * value


result = target_function('red', 10)
print(("RESULT is", result))
print(('-' * 50))
result = target_function('green', 45)
print(("RESULT is", result))
print(('-' * 50))
print()
print()


def func_deco_class(target_class):
    """
    function without params decorating a class

    :param target_class: class to be decorated
    :return: modified class
    """
    print("GREETINGS from func_deco_class!")
    @property
    def _temp(self):
        return self._value1

    target_class.value_one = _temp

    return target_class


def func_deco_class_param(fruit):
    """
    function with params decorating a class; returns wrapper which is applied to target class

    :param fruit:
    :return: modified class
    """
    print("GREETINGS from func_deco_class_param!")

    def wrapper(target_class):

        target_class._fruit = fruit

        @property
        def _temp(self):
            return self._fruit

        target_class.fruit = _temp

        return target_class

    return wrapper



@func_deco_class
@func_deco_class_param('MANGO')
class target_class(object):

    def __init__(self, v1, v2, v3, v4):
        self._value1 = v1
        self._value2 = v2
        self._value3 = v3
        self._value4 = v4


t1 = target_class('fee', 'fi', 'fo', 'fum')
print(("t1 is", t1))
print("value1:", t1._value1)
print(("value_one:", t1.value_one))

print(('-' * 50))
t2 = target_class('eeny', 'meeny', 'miny', 'mo')
print(("t2:", t2))
print(("t2.value_one:", t2.value_one))
print(("t2.fruit:", t2.fruit))

print(('-' * 50))


class class_deco_class(object):
    """
    class without params decorating a class

    __new__() returns the modified class (not __init__, because __init__ is *instance* initializer)

    """
    def __new__(cls, old_class):
        print("GREETINGS from class_deco_class!")
        old_class.color = 'blue'
        return old_class


@class_deco_class
class target_class(object):
    pass


t1 = target_class()
print((t1.color))
print(("t1 id:", id(t1)))
print((target_class.__name__, t1))

t2 = target_class()
print((t2.color))
print(("t2 id:", id(t2)))

print(('-' * 50))


class class_deco_class_param(object):
    """
    class with params decorating a class

    __call__() returns the modified class
    """

    def __init__(self, color):
        print("GREETINGS from class_deco_class_param!")
        self._color = color

    def __call__(self, old_class):
        old_class.color = self._color
        return old_class


@class_deco_class_param('purple')
class target_class(object):
    pass


t1 = target_class()
print((t1.color))
