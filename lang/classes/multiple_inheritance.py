#!/usr/bin/env python


# Primary base class
class AnimalBase():

    def __init__(self, name):
        self._name = name

    def id(self):
        print(self._name)


# Additional (mixin) base class
class CanBark():

    def bark(self):
        print("woof-woof")


# Additional (mixin) base class
class CanFly():

    def fly(self):
        print("I'm flying")


# Inherit from primary base class plus mixin
class Dog(CanBark, AnimalBase):
    pass


# Inherit from primary base class plus mixin
class Sparrow(CanFly, AnimalBase):
    pass


d = Dog('Dennis')
d.id()  # All animals have id()
d.bark()  # Dog can bark() (from CanBark mixin)
print()

s = Sparrow('Steve')
s.id()  # All animals have id()
s.fly()  # Sparrow can fly() (from CanFly mixin)
print()

# MRO Method Resolution Order
print("Sparrow mro:", Sparrow.mro())
# Sparrow mro: [<class '__main__.Sparrow'>, <class '__main__.CanFly'>, <class'__main__.AnimalBase'>, <class 'object'>]

