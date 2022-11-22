#!/usr/bin/env python

"""
Classes
    Represents a thing (such as file, process, database record, strategy, string, person, truck, etc.)
    Encapsulates functions and variables
    Creator of object instances
    Basic unit of object-oriented programming
    Class describes
        Data
            Class data
                Shared by all instances of the class
            Instance data
                Represents one instance of the thing and only accessible from that instance
        Methods
            Functions that act upon the data
    Note
        If you just need some functions, and they don't need to share or remember data, just put the functions in a module.
        If you just need some data, but don't need functions to process it, just use a nested structure (dictionaries, lists, tuples).
    Syntax
        class ClassName(base_class,...):
            # class body - methods and data
    StudlyCaps for ClassName
    Class definition creates a new local namespace
    All variable assignments go into this new namespace
    All methods are called via the instance or the class name
    Base classes
        List of base classes may be specified in parentheses after the class name
    No access modifiers - everything in Python class is public although underscore indicates private like javascript
    Special methods
        __init__ constructor method - hidden by default but can be overridden
        __str__ string method, similar to toString in Java
"""
# Simplest form of a class definition
class ClassName():
    pass


"""
Object Instances
    Class class name as a function
    self contains attributes
    Syntax
        obj = ClassName(args...)
    Methods and data accessed using dot notation (e.g. obj_instance.some_method())
    Instance attributes are dynamic; they can be accessed directly from the object. You can create, update, and delete attributes in this way.
    Each object instance has its own private attributes, which are usually created in the __init__ method.
    Privacy by convention (_name)
    Attributes cannot be made private, but names that begin with an underscore are understood by convention to be for internal use only.
    Users of your class will not consider methods that begin with an underscore to be part of your class's API.
    In most cases, it is better to use properties to access data attributes
"""
class Spam():

    def eggs(self):
        pass

    # private
    def _beverage(self):
        pass


s = Spam()
s.eggs()

# Dynamic attributes; create new instance attribute on the fly
s.toast = 'buttered'
print(s.toast)

# Legal, but WRONG!
s._beverage()


"""
Instance Methods
    Called from objects
    Object is implicit parameter
    An instance method is a function defined in a class. When a method is called from an object, the object is passed
    in as the implicit first parameter, named self by strong convention.

Constructors
    Optional
    Named __init__
    If class defines method named __init__ it will be automatically called when an object instance is created
    The object being created is implicitly passed as the first parameters to __init__
    Named self by strong convention (same as this in C++, Java, C#)
    Data attributes can be assigned to self
    These attributes can then be accessed by other methods
"""
class Rabbit:

    # Constructor, passed self
    def __init__(self, size, danger):
        self._size = size
        self._danger = danger
        self._victims = []

    # Instance method, passed self
    def threaten(self):
        print("I am a {} bunny with {}!".format(self._size, self._danger))


# Pass parameters to constructor
r1 = Rabbit('large',"sharp, pointy teeth")
# Instance method as access to variables via self
r1.threaten()

r2 = Rabbit('small','fluffy fur')
r2.threaten()


"""
Getters and Setters
    Used to access data
    AKA accessors and mutators
    Getter
        Retrieves data (a private variable) from self
    Setter
        Assigns value to variable (usually a private variable)
    Note
        Most developers use properties instead of getters and setters
"""
class KnightGetterSetter(object):

    # Constructor initialize private attribute
    def __init__(self, name):
        self._name = name


    # Set private variable
    def set_name(self, name):
        self._name = name


    # Get private variable
    def get_name(self):
        return self._name


k = KnightGetterSetter('Lancelot')
print(k.get_name())


"""
Properties
    Accessed like variables
    Invoke implicit getters and setters
    Can be read-only
    Object attributes can be accessed directly, but in many cases class needs to exercise some control over the attributes
    Property is kind of managed attribute
    It is accessed directly just as normal attributes, but getter, setter and deleter functions are implicitly called
    Getter Property
        Must be created first
        Apply @property decorator to a method with the name you want
        Method receives no parameters other than self
    Setter Property
        Create another function with the property name (yes there will be two function definitions with the same name)
        Decorate with property name plus '.setter' (e.g. @spam.setter)
        Method will take one parameter (other than self) which is the value assigned to the property
        It is common for a setter proeprty to raise an error if the value being assigned is invalid
    Deleter Property
        Seldom needed
        Same as setter property
        Decorate with '@propertyname.deleter'
"""
class Knight(object):
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color

    # Getter property decorator
    @property
    def name(self):  # Property implemented by name() method
        return self._name

    @property
    def color(self):
        return self._color

    # Setter property decorator
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be a string")


if __name__ == '__main__':
    k = Knight("Lancelot", "Sir", 'blue')

    # Bridgekeeper's question
    print('Sir {}, what is your...favorite color?'.format(k.name))  # Using property

    # Knight's answer
    print("red, no -- {}!".format(k.color))

    k.color = 'red'  # Setting property

    print("color is now:", k.color)


"""
Class Data
    Attached to class, not instance
    Shared by all instances
    Accessed via the class name from inside or outside of the class
    Any class attribute not overwritten by an instance attribute is also available through the instance

Class Methods
    Called from class or instance
    Decorate method with @classmethod to define
    This alters the method so that it gets a copy of the class object rather than the instance object
    This is true whether the method is called rom the class or from an instance
    First (implicit) parameter named "cls" by convention

Static Methods
    Related to class, but doesn't need instance or class object
    Use @staticmethod decorator
    A static method is a utility method that is related to the class, but does not need the instance or class object. Thus, it has no automatic parameter.
    One use case for static methods is to factor some kind of logic out of several methods, when the logic doesn't require any of the data in the class.
    Note
        Static methods are seldom needed
"""
class Rabbit:

    # Class data
    LOCATION = "the Cave of Caerbannog"

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        # Look up class data via instance
        print("This rabbit guarding {} uses {} as a weapon".format(self.LOCATION, self.weapon))

    # Class method
    @classmethod
    def get_location(cls):  # Receives copy of class object 'cls'
        # Access class data
        return cls.LOCATION

    # Static method
    @staticmethod
    def static_method():
        print('static method')


r1 = Rabbit("a nice cup of tea")
# Instance method uses class data
r1.display()

r2 = Rabbit("big pointy teeth")
# Instance method uses class data
r2.display()

# ClassName.ClassData
print(Rabbit.LOCATION)

# ClassName.classmethod
print(Rabbit.get_location())

# Instance.classmethod
print(r1.get_location())

# ClassName.staticmethod
print(Rabbit.static_method())

# Instance.staticmethod
print(r1.static_method())

"""
Special Methods
    User-defined classes emulate standard types
    Define behavior for builtin functions
    Override operators
    Expect self parameter, like all instance methods
    self is the object being called from the builtin function, or left operand of a binary operator such as ==
    Frequently take one or more additional parameters.
    Example
        Have str() return hostanme, port of a database connection rather than something like <main.DBConn object at 0x782c6c>
    Ref
        http://docs.python.org/reference/datamodel.html#special-method-names for detailed documentation on the special methods.

Method or Variables                 Description
------------------------------------------------
__new__(cls,...)                    Returns new object instance; Called before __init__()
__init__(self,...)                  Object initializer (constructor)
__del__(self )                      Called when object is about to be destroyed
__repr__(self )                     Called by repr() builtin
__str__(self )                      Called by str() builtin
------------------------------------------------
__eq__(self, other)                 Implement comparison operators ==, !=, >, <, >=, and ⇐. self is object on the left.
__ne__(self, other)
__gt__(self, other)
__lt__(self, other)
__ge__(self, other)
__le__(self, other)
------------------------------------------------
__cmp__(self, other)                Called by comparison operators if __eq__, etc., are not defined
__hash__(self )                     Called by hash() builtin, also used by dict, set, and frozenset operations
__bool__(self )                     Called by bool() builtin. Implements truth value (boolean) testing. If not present, bool() uses len()
__unicode__(self )                  Called by unicode() builtin
------------------------------------------------
__getattr__(self, name)             Override normal fetch, store, and deleter
__setattr__(self, name, value)
__delattr__(self, name)
------------------------------------------------
__getattribute__(self, name)        Implement attribute access for new-style classes
__get__(self, instance)             __set__(self, instance, value)
__del__(self, instance)             Implement descriptors
__slots__ = variable-list           Allocate space for a fixed number of attributes.
__metaclass__ = callable            Called instead of type() when class is created.
__instancecheck__(self, instance)   Return true if instance is an instance of class
__subclasscheck__(self, instance)   Return true if instance is a subclass of class
__call__(self, ...)                 Called when instance is called as a function.
__len__(self )                      Called by len() builtin
__getitem__(self, key)              Implements self[key]
__setitem__(self, key, value)       Implements self[key] = value
__selitem__(self, key)              Implements del self[key]
__iter__(self )                     Called when iterator is applied to container
__reversed__(self )                 Called by reversed() builtin
__contains__(self, object)          Implements in operator
------------------------------------------------
__add__(self, other)                Implement binary arithmetic operators +, -, *, //, %, **, <<, >>, &, ^, and |. Self is object on left side of expression.
__sub__(self, other)
__mul__(self, other)
__floordiv__(self, other)
__mod__(self, other)
__divmod__(self, other)
__pow__(self, other[, modulo])
__lshift__(self, other)
__rshift__(self, other)
__and__(self, other)
__xor__(self, other)
__or__(self, other)
------------------------------------------------
__div__(self,other)                 Implement binary division operator /. __truediv__ is called if __future__.division is in effect.
__truediv__(self,other)
------------------------------------------------
__radd__(self, other)               Implement binary arithmetic operators with swapped operands. (Used if left operand does not support the corresponding operation)
__rsub__(self, other)
__rmul__(self, other)
__rdiv__(self, other)
__rtruediv__(self, other)
__rfloordiv__(self, other)
__rmod__(self, other)
__rdivmod__(self, other)
__rpow__(self, other)
__rlshift__(self, other)
__rrshift__(self, other)
__rand__(self, other)
__rxor__(self, other)
__ror__(self, other)
------------------------------------------------
__iadd__(self, other)               Implement augmented (+=, -=, etc.) arithmetic operators
__isub__(self, other)
__imul__(self, other)
__idiv__(self, other)
__itruediv__(self, other)
__ifloordiv__(self, other)
__imod__(self, other)
__ipow__(self, other[, modulo])
__ilshift__(self, other)
__irshift__(self, other)
__iand__(self, other)
__ixor__(self, other)
__ior__(self, other)
------------------------------------------------
__neg__(self )                      Implement unary arithmetic operators -, +, abs(), and ~
__pos__(self )
__abs__(self )
__invert__(self )
------------------------------------------------
__oct__(self )                      Implement oct() and hex() builtins
__hex__(self )
------------------------------------------------
__index__(self )                    Implement operator.index()
__coerce__(self, other)             Implement "mixed-mode" numeric arithmetic.
"""
print('--> Special Methods')
class Special(object):

    def __init__(self, value):
        # All Special instances are strings
        self._value = str(value)

    # Define what happens when a Special instance is added by a value
    def __add__(self, other):
        return self._value + other._value

    # Define what happens when a Special instance is multiplied by a value
    def __mul__(self, num):
        return ''.join((self._value for i in range(num)))

    # Define what happens when str() called on a Special instance
    def __str__(self):
        return self._value.upper()

    # Define equality between two Special values
    def __eq__(self, other):
        return self._value == other._value


if __name__ == '__main__':
    s = Special('spam')
    t = Special('eggs')
    u = Special('spam')
    v = Special(5)  # Parameter to Special() is converted to a string
    w = Special(22)

    print("s + s", s + s)  # Add two Special instances
    print("s + t", s + t)
    print("t + t", t + t)
    print("s * 10", s * 10)  # Multiply a Special instance by an integer
    print("t * 3", t * 3)
    print("str(s)={}  str(t)={}".format(str(s), str(t)))
    print("id(s)={} id(t)={} id(u)={}".format(id(s), id(t), id(u)))
    print("s == s", s == s)
    print("s == t", s == t)
    print("s == u", s == u)
    print("v + v", v + v)
    print("v + w", v + w)
    print("w + w", w + w)
    print("v * 10", v * 10)
    print("w * 3", w * 3)


global_var = []

class MyClass:
    # pass # keyword in Python tells interpreter 'do nothing' good for temp placeholder

    # Don't need an instance in order to call a static var (ex. MyClass.a_static_variable).
    a_static_variable = "This value will be the same for every class"

    # Constructor method
    # Provided by default and hidden, but can be overridden
    def __init__(self, instance_attribute, optional_arg=22):
        self.instance_attribute = instance_attribute
        self.optional_arg = optional_arg
        global_var.append(self)
        print("__init__ called", instance_attribute)

    # Method must have first parameter, usually called self.
    def class_method(self):
        print("class_method called")

    def common_method(self):
        print("common_method in parent class")
        return "Parent"

    # Override string method
    def __str__(self):
        return "I've overridden __str__ " + self.instance_attribute


# Inherit a class by passing BaseClass/ParentClass in parenthesis
class ChildClass(MyClass):
    a_static_variable = "Overwritten Parent value in ChildClass"

    def common_method(self):
        parent_value = super().common_method()
        print("common_method in child class, but parent value is {0}".format(parent_value))


if __name__ == '__main__':
    # Instantiate a new class
    my_class = MyClass("required_arg")
    print("Instantiate a new class:{0}".format(my_class))

    # Don't need an instance in order to call a static var (ex. MyClass.a_static_variable).
    print("MyClass.a_static_variable:{0}".format(MyClass.a_static_variable))

    # Instantiate a new child class
    a_child = ChildClass("child class is using parent constructor")
    print("Instantiate a new child class:{0}".format(a_child))

    print("ChildClass.a_static_variable:{0}".format(ChildClass.a_static_variable))

    print('# a_child.class_method()')
    a_child.class_method()

    print('# a_child.common_method()')
    a_child.common_method()