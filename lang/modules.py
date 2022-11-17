"""
Modules
    import keyword
    Can import classes, method, attributes
"""
# import means you'll need to prefix every reference classes.<the class i want>
import classes

# alternate syntax so you don't need to prefix classes
from classes import ChildClass  # can also use * to import everything

a_class = classes.MyClass("imported module")
a_child = ChildClass("imported module")