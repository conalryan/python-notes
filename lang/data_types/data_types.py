"""
Data Types
    Python3 source encoding is UTF-8
    Dynamically-Typed language
    Integers
    Floats
    String
    Bytes
    bool - Logical True of False. bool(1) == True bool(0) == False
    None - Absence of value
    int() to cast to int
    float() to cast to float
"""

"""
Compare var declarations:
    - C# or Java:
    [type] [varName] = [value]
    int anInt = 42;
    String aString = "I'm a string";

    - Python:
    [var_name] = [value]
    an_int = 42
    a_string = "I'm a string"
"""
an_int = 42
a_float = 22.22
a_string = "I'm a string"
a_bool = True
a_byte = b'a byte'
a_none = None

"""
TypeErrors
    Similar to JS you can get Type errors
"""
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 11)  # prints 16

# add_numbers(5, "something") # TypeError: unsupported operand type(s) for +: 'int' and 'str'


"""
Type-Hinting added in 3.5
    This is only helping your IDE, there is no check in the language itself
"""
def add_numbers_hint(a: int, b: int) -> int:
    return a + b


""""
Integers
  int
  Unlimited precision
  Signed integer
"""
a_positive_integer = 22
a_negative_integer = -22


""""
Floats
    float
    IEE-754 double precision floating-point numbers with 53 bits of binary precision.
    This is equivalent to between 15 and 16 significant digits in decimal. 
"""
a_positive_float = 3.14159
a_negative_float = -23.56

# Conversion - wrap in int() or float()
print(int(a_positive_float))  # 3
print(float(a_negative_integer))  # -22.0


""""
Boolean 
    Starts with capital letter True or False
"""
a_positive_boolean = True
a_negative_boolean = False

# Similar to C++ cast boolean to int
an_int_from_bool = int(a_positive_boolean)  # == 1
another_int_from_bool = int(a_negative_boolean)  # == 0
a_string_from_bool = str(a_positive_boolean)  # == "True"


""""
None
    Similar to null but will not throw error
    Good to use as a placeholder where a value is not set yet
    It will evaluate to false in boolean check
"""
a_none_variable = None


"""
Exceptions
    try:
        # try something
    except SomeError:
        # do something with exception
    KeyError, IndexError, TypeError etc
"""
a_dictionary = {'key': 22, 'another_key': 'another_value'}
try:
    the_value = a_dictionary["key_that_doesnt_exist"]
except KeyError:
    print("error getting the key")
# chain exceptions, can also pass error object
except TypeError as error:
    print("chaining errors")
    print(error)
# generic catch all
except Exception:
    print("catch anything and everything")


"""
Other Data Types
    complex
    long # only in Python 2
    bytes
    bytearray
    tuple = (3, 5, 1, "Mark")
    set
    frozenset
    set([3 , 2, 3, 1, 5]) == (1, 2, 3, 5)
"""


"""
Builtins
    Python automatically imports __builtins__ when interpreter starts
    len
    min
    max
"""
fruits = ['apple', 'banana', 'cherry']
print(__builtins__.len(fruits))
print(len(fruits))

print(len(fruits), min(fruits), max(fruits))