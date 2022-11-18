"""
Functions
    Block of organized and reusable code that is used to perform a certain actions
    Generally function should do only 1 thing
    Built-in
        print()
        int()
        str()
        len()
        input()
        etc...
    'def' keyword used to specify function
    Use double line spaces between functions definitions
    Parameters
        Parameter types are dynamic
        Positional or named
        Required or optional
        Default
            Assigned with equals sign (e.g. func(some_default_param=22))
            Used if no value is passed to function
            Parameters without defaults cannot be specified after parameters with defaults
        First
            Positional
            Required
            Comma-separated names
        Second
            Positional
            Optional
            Preceded by asterisk *
        Third
            Named
            Required
            Aka Keyword-only
            If there are no optional parameters you can use a plain asterisk as a placeholder
        Fourth
            Named
            Optional
            Preceded by two asterisks **
        Example:
            def func(p1, p2, *p3, p4, p5, **p6)
                # p1 and p2 are positional required
                # *p3 is positional optional
                # p4, p5 are named required (aka Keyword-only)
                # **p6 are named optional
                pass
    Return
        A value/object of any type
        If there is no return statement, function returns None.
"""


def my_function():
    print("my function is doing stuff")
    return 22  # Optional return statement. If not provided it will return None.


# arg is block scoped to function
# must call function with same number of args as declaration
def my_function_with_arg(some_arg):
    print('--> my_function_with_arg')
    print(some_arg)
    print()


my_function_with_arg("what up")


# default arg
def default_arg_function(arg_1, arg_2=123):
    print('--> default_arg_function')
    print(arg_1, arg_2)
    print()


# uses default arg
default_arg_function("first arg")

# overrides default arg
default_arg_function("first arg", 999)

# named args
default_arg_function(arg_1="I named it", arg_2=22)


def variable_number_of_args(arg_1, *var_args):
    print('--> variable_number_of_args')
    print(arg_1)
    print(var_args)
    print()


variable_number_of_args("first arg", "var arg 2", 22, None, True)


# keyword args - becomes dictionary inside function
def keyword_args(**key_word_args):
    print('--> keyword_args')
    print(key_word_args["first_key_word_arg"], key_word_args["next_key"], key_word_args["yet_another_thing"])
    print()


keyword_args(first_key_word_arg="the first one", next_key="another key", yet_another_thing=22)


# One required parameter
def func_required_param(n):
    print('--> func_required_param(n)')
    return n ** 2


x = func_required_param(5)
print("func_required_param(5) is {}\n".format(x))


# One required parameter with default value
def func_required_default(count=3):
    print('--> func_required_default(count=3)')
    for i in range(count):
        print("spam", end=' ')
    print()


func_required_default()
print()
func_required_default(10)
print()


# One fixed, one optional
def func_fixed_optional(n, *opt):
    print("func_fixed_optional(n, *opt):")
    print("n is ", n)
    print("opt is", opt)
    print()


func_fixed_optional('apple')
func_fixed_optional('apple', "blueberry", "peach", "cherry")


# Keyword-only parameters
def func_keyword_only(*, spam=0, eggs=0):
    print("func_keyword_only(*, spam=0, eggs=0):")
    print("spam is:", spam)
    print("eggs is:", eggs)
    print()


func_keyword_only(spam=1, eggs=2)
func_keyword_only(eggs=2, spam=2)
func_keyword_only(spam=1)
func_keyword_only(eggs=2)
func_keyword_only()


# Keyword (named) parameters
def func_keyword_name(**named_args):
    print("func_keyword_name(**named_args):")
    print(named_args)
    for name in named_args:
        print(name,"==> ",named_args[name])
    print()


func_keyword_name(name="Lancelot", quest="Grail", color="red")


# Nested Functions
# Closure
#   inner_function has access to outer_functions scopes
def outer_function():
    print('--> Nested functions (Closure)')
    outer_var = "I'm outer"
    print(outer_var)

    # inner_function has access to outer_function scopes (ie. closure)
    def inner_function():
        print("I'm inside the inner function but the outer_var is: {0}".format(outer_var))
        return "inner function called yo"

    outer_var = inner_function()
    print(outer_var)
    print()


outer_function()


# Generator Functions - Yield
# This function will read in the file lines and yield a single line out to the caller
def read_lines(file):
    for line in file:
        yield line


# The for loop will trigger the generator to kick off again
def read_file():
    try:
        f = open("data/some_file.txt", "r")
        for some_text in read_lines(f):
            print(some_text)
        f.close()
    except Exception:
        print("Error opening file")


read_file()

"""
Lambda Functions
    Anonymous functions
    Very short, 1 line, can take args
    Used in higher level functions - functions that take functions as an arg
"""


# same as double_lambda
def double_def(x):
    return x * 2


# same as double_def()
double_lambda = lambda x: x * 2


print(double_def(5))

print(double_lambda(5))