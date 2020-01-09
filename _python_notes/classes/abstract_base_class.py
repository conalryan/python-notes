#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

"""
Abstract Base Class
    Designed for inheritance
    Abstract methods must be implemented
    Decorated with '@abstractmethod'
    Assign ABCMeta to the class option metaclass
    Non-abstract methods may be overwritten
    abc module also provides decorators for abstract properties and abstract class methods
"""
# Metaclasses control how classes are created; ABCMeta adds restrictions to classes that inherit from Animal
class Animal(metaclass=ABCMeta):

    # When decorated with @abstractmethod, speak() becomes an abstract method
    @abstractmethod
    def speak(self):
        pass


# Inherit from abstract base class Animal
class Dog(Animal):

    # speak() must be implemented
    def speak(self):
        print("woof! woof!")


# Inherit from abstract base class Animal
class Cat(Animal):

    # speak() must be implemented
    def speak(self):
        print("Meow meow meow")


# Inherit from abstract base class Animal
class Duck(Animal):
    # Duck does not implement speak()
    pass


d = Dog()
d.speak()

c = Cat()
c.speak()

try:
    # Duck throws a TypeError if instantiated since it did not implement abstract method
    d = Duck()
    d.speak()
except TypeError as err:
    print(err)  # Can't instantiate abstract class Duck with abstract methods speak
