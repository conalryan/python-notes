#!/usr/bin/env python

"""
Numeric Types:
    - bool
    - int
    - float
    - complex
"""


"""
bool
    Boolean 
    Starts with capital letter True or False
"""
a_positive_boolean = True
a_negative_boolean = False

# Similar to C++ cast boolean to int
print(int(a_positive_boolean))  # 1
print(int(a_negative_boolean))  # 0
print(str(a_positive_boolean))  # "True"


"""
int
    Integer
    Unlimited precision
    Signed integer
"""
a_positive_integer = 22
a_negative_integer = -22


""""
float
    Float
    IEE-754 double precision floating-point numbers with 53 bits of binary precision.
    This is equivalent to between 15 and 16 significant digits in decimal. 
"""
a_positive_float = 3.14159
a_negative_float = -23.56

# Conversion - wrap in int() or float()
print(int(a_positive_float))  # 3
print(float(a_negative_integer))  # -22.0
