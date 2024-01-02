# Naming:
# Here are some common naming conventions used in Python

# 1. Name: snake_case
#    Description: Every character is lowercase and words are separated by underscores.
#    Usage area: Variables, file names, function names.
#    Example: my_variable, my_file.txt, my_function_name

# 2. Name: UPPER_CASE
#    Description: All characters are uppercase and words are separated by underscores.
#    Usage area: Constants and module-level variables.
#    Example: MAX_VALUE, CONFIG_FILE_NAME

# 3. Name: PascalCase
#    Description: The first character of each word is capitalized and there are no spaces or underscores between words.
#    Usage area: Class names, method names, and module names.
#    Example: MyClass, SomeFunction, MyModule

# 4. Name: camelCase (also known as mixedCase) (not common in python)
#    Description: The first character of the first word is lowercase and the first character of each subsequent word is capitalized. There are no spaces or underscores between words.
#    Usage area: Variable names, function names.
#    Example: myVariable(objects), myFunction

# 5. Name: _single_leading_underscore
#    Description: This convention is used to indicate that a variable or method is intended for internal use. It's a signal to other developers that the variable or method is private and should not be accessed directly.
#    Usage area: Private variables and methods inside a class.
#    Example: _private_variable, _private_method

# 6. Name: __double_leading_underscore
#    Description: By prefixing a name with two underscores, Python invokes name mangling, which can be used to avoid name clashes with subclasses.
#    Usage area: Name mangling in class definitions.
#    Example: __private_variable, __private_method

# 7. Name: dunder (double underscore) 
#    Description: The term "dunder" is short for "double underscore" and is used to refer to special methods or attributes in Python. These are often used for built-in methods like `__init__`, `__str__`, `__repr__`, etc.
#    Usage area: Special methods and attributes.
#    Example: __init__, __str__, __repr__


# Naming conventions in Python

# 1. snake_case examples
my_variable = 10
my_file = open('my_file.txt', 'w')
def my_function_name():
    pass

# 2. UPPER_CASE examples
MAX_VALUE = 100
CONFIG_FILE_NAME = 'config.txt'

# 3. PascalCase examples
class MyClass:
    pass

def SomeFunction():
    pass

MyModule = 'my_module'

# 4. camelCase examples (not commonly used in Python)
def myFunction(objects):
    pass

myVariable = 'value'

# 5. _single_leading_underscore examples
class MyClass:
    _private_variable = 42
    def _private_method(self):
        pass

# 6. __double_leading_underscore examples
class MyClass:
    def __private_method(self):
        pass

# 7. dunder or double underscore examples
class MyClass:
    def __init__(self):
        pass
    
    def __str__(self):
        return "MyClass instance"

    def __repr__(self):
        return "MyClass()"