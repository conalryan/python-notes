#!/usr/bin/env python

"""
Creating Classes at Runtime
    Use the type() function
    Provide dictionary of attributes
    For advanced needs, a class can be created programmatically, without the use of the class statement
    Syntax
        type("name", (base_class, ...), {attributes})
    First arg is the name of the class
    Second arg is a tuple of base classes (use object if you are not inheriting from a specific class)
    Third arg is a dictionary of the class's attributes

"""
# Create method (not inside a class - could be a lambda)
def f1(self):
    print("Hello from f1()")


# Create method (not inside a class - could be a lambda)
def f2(self):
    print("Hello from f2()")


# Create class using type() - parameters are class name, base class(es), dictionary of attributes
new_class = type("new_class", (object,), {
    'hello1': f1,
    'hello2': f2,
    'color': 'red',
    'state': 'Ohio',
})


# Create instance of new class
n1 = new_class()

# Call instance method
n1.hello1()
n1.hello2()

# Access class data
print(n1.color)
print()

# Create subclass of first class
sub_class = type("sub_class", (new_class,), {'fruit': 'banana'})

# Create instance of subclass
s1 = sub_class()

# Call method on subclass
s1.hello1()

# Access class data
print(s1.color)
print(s1.fruit)
