"""
Object Oriented Programming

Classes
    Logical group of methods and data
    You don't have to write Python inside classes but you can
    'class' keyword
    Instantiate by calling class name (ex. MyClass())
    Special methods
        __init__ constructor method - hidden by default but can be overridden
        __str__ string method, similar to toString in Java
    Static methods and variables
    Instance attributes
    No access modifiers - everything in Python class is public
"""
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


# Instantiate a new class
print('### Instantiate a new class:')
my_class = MyClass("required_arg")
print(my_class)

# Don't need an instance in order to call a static var (ex. MyClass.a_static_variable).
print('### MyClass.a_static_variable:')
print(MyClass.a_static_variable)


# Inherit a class by passing BaseClass/ParentClass in parenthesis
class ChildClass(MyClass):
    a_static_variable = "Overwritten Parent value in ChildClass"

    def common_method(self):
        parent_value = super().common_method()
        print("common_method in child class, but parent value is {0}".format(parent_value))


# Instantiate a new child class
print('### Instantiate a new child class:')
a_child = ChildClass("child class is using parent constructor")
print(a_child)

print('### ChildClass.a_static_variable')
print(ChildClass.a_static_variable)

print('### a_child.class_method()')
print(a_child.class_method())

print('### a_child.common_method()')
print(a_child.common_method())