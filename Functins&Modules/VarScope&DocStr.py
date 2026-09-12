# # Variable Scope and Docstrings
# In Python, variables have scope (where they can be accessed) and lifetime (how long they exist). Variables are created when a function is called and destroyed when it returns. Understanding scope helps avoid unintended errors and improves code organization.

# Types of Scope in Python
# Local Scope (inside a function) – Variables declared inside a function are accessible only within that function.
# Global Scope (accessible everywhere) – Variables declared outside any function can be used throughout the program.
# Example:
# x = 10  # Global variable
 
# def my_func():
#     x = 5  # Local variable
#     print(x)  # Output: 5
 
# my_func()
# print(x)  # Output: 10 (global x remains unchanged)

# Using the global Keyword
# To modify a global variable inside a function, use the global keyword:

# x = 10  # Global variable
 
# def modify_global():
#     global x
#     x = 5  # Modifies the global x
 
# modify_global()
# print(x)  # Output: 5

# This allows functions to change global variables, but excessive use of global is discouraged as it can make debugging harder.

# 7. Docstrings - Writing Function Documentation
# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute. Here's an example:

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
 
# print(add.__doc__)  # Output: Returns the sum of two numbers.

# Here is even proper way to write docstrings:

# def add(a, b):
#     """
#     Returns the sum of two numbers.
 
#     Parameters:
#     a (int): The first number.
#     b (int): The second number.
 
#     Returns:
#     int: The sum of the two numbers.
#     """
#     return a + b

# Summary
# Functions help in reusability and modularity.
# Functions can take arguments and return values.
# Lambda functions are short, inline functions.
# Recursion is a technique where a function calls itself.
# Modules help in organizing code and using external libraries.
# Scope and lifetime of variables decide their accessibility.
# # Docstrings are used to document functions, classes, and modules.