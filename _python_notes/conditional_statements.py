"""
Conditional Statements
"""

"""
if Statements
    Colon at end of if and end of else
    Double == for equality check
    != to negate (i.e. if my_value != 22: # my value is not 22)
    'not' keyword to negate (i.e if not some_boolean: ) can't use ! to negate
    'is' keyword to check if variables are pointing to the same memory location
    'is not' for opposite of 'is'
    'and' keyword to add condition, both must be truthy, don't use &&
    'or' keyword to add condition, one must be truthy, don't use ||
    Truthy Values
        Any number != 0
        Any string that is not empty (including 'False')
        Any list that is not empty
    Falsey Values
        False
        Any number == 0
        Empty string
        Empty list
        Empty tuple
        Empty dict
        Empty set()
        None

if <some_condition>:
    # do stuff
elif <some_other_condition>:
    # do other stuff
else:
    # do something else
    
Pseudo ternary
some_value = if <some_condition> else some_other_value
"""


# equality
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")


# not-equal
if number != 22:
    print("The number is not 22")


# Truthy
truthy_number = 22
if truthy_number:
    print("The number is truthy")


# Falsey
falsey_number = 0
if not falsey_number:
    print("The number is falsey")


# And Or
# use keywords 'and' 'or' not && ||
if number == 5 and truthy_number != 0:
    print("and")

if number == 6 or not falsey_number:
    print("or")


# Ternary if Statements
a = 1
b = 2
c = "bigger" if a > b else "smaller"
print(c)


# if elif else
value = 65
if value > 30:
    print('yup')
elif value > 50:
    print('sure')
else:
    print('nope')