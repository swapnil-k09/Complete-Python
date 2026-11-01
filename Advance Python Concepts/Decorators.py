# Decorators in Python
# Decorators in Python are a powerful and expressive feature that allows you to modify or enhance functions and methods in a clean and readable way. They provide a way to wrap additional functionality around an existing function without permanently modifying it. This is often referred to as metaprogramming, where one part of the program tries to modify another part of the program at compile time.

# Decorators use Python's higher-order function capability, meaning functions can accept other functions as arguments and return new functions.

# Understanding Decorators
# A decorator is simply a callable (usually a function) that takes another function as an argument and returns a replacement function. The replacement function typically extends or alters the behavior of the original function.

# Basic Example of a Decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
 
# @my_decorator
# def say_hello():
#     print("Hello!")
 
# say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
# Here, @my_decorator is syntactic sugar for say_hello = my_decorator(say_hello). It modifies the behavior of say_hello() by wrapping it inside wrapper(). The wrapper function adds behavior before and after the original function call.

# Using Decorators with Arguments
# Decorators themselves can also accept arguments. This requires another level of nesting: an outer function that takes the decorator's arguments and returns the actual decorator function.

# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for _ in range(n):
#                 func(a)
#         return wrapper
#     return decorator
 
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
 
# greet("world")

# Output:
# Hello, world!
# Hello, world!
# Hello, world!
# In this example, repeat(3) returns the decorator function. The @ syntax then applies that returned decorator to greet. The argument in the wrapper function ensures that the decorator can be used with functions that take any number of positional and keyword arguments.

# Chaining Multiple Decorators
# You can apply multiple decorators to a single function. Decorators are applied from bottom to top (or, equivalently, from the innermost to the outermost).

# def uppercase(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
 
# def exclaim(func):
#     def wrapper():
#         return func() + "!!!"
#     return wrapper
 
# @uppercase
# @exclaim
# def greet():
#     return "hello"
 
# print(greet())

# Output:
# HELLO!!!
# Here, greet is first decorated by exclaim, and then the result of that is decorated by uppercase. It's equivalent to greet = uppercase(exclaim(greet)).

# Recap
# Decorators are a key feature in Python that enable code reusability and cleaner function modifications. They are commonly used for:

# Logging: Recording when a function is called and its arguments.
# Timing: Measuring how long a function takes to execute.
# Authentication and Authorization: Checking if a user has permission to access a function.
# Caching: Storing the results of a function call so that subsequent calls with the same arguments can be returned quickly.
# Rate Limiting: Controlling how often a function can be called.
# Input Validation: Checking if the arguments to a function meet certain criteria.
# Instrumentation: Adding monitoring and profiling to functions.
# Frameworks like Flask and Django use decorators extensively for routing, authentication, and defining middleware.


# def decorator(function):
#     def wrapper():
#         print("Hello!")
#         function()
#         print("bye!")
#     return wrapper
# @decorator #...
# def ask():
#     print("How are you?")
# ask()
# a = decorator(ask)
# a()


# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
# @repeat(5)
# def Hello():
#     print("Hello!")
# Hello()

#/////////////////////////
# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator
# @repeat(5)
# def Hello(a):
#     print("Hello!", a)
# Hello("SK!")