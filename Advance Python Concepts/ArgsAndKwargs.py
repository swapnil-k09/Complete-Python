# Args and kwargs
# *args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function. They are used when you don't know in advance how many arguments a function might need to accept.

# *args: Allows you to pass a variable number of positional arguments.
# **kwargs: Allows you to pass a variable number of keyword arguments.
# *args (Positional Arguments)
# *args collects any extra positional arguments passed to a function into a tuple. The name args is just a convention; you could use any valid variable name preceded by a single asterisk (e.g., *values, *numbers).

def my_function(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)
 
my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
my_function()  # No output (empty tuple)
my_function("a", "b")  # Output: a b

# In this example, *args collects all positional arguments passed to my_function into the args tuple.

# **kwargs (Keyword Arguments)
# **kwargs collects any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data, **options).

def my_function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
 
my_function()  # No output (empty dictionary)
my_function(a=1, b=2)
# Output:
# a: 1
# b: 2

# In this example, **kwargs collects all keyword arguments into the kwargs dictionary.

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function definition. The order is important: *args must come before **kwargs. You can also include regular positional and keyword parameters.

def my_function(a, b, *args, c=10, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")
 
my_function(1, 2, 3, 4, 5, c=20, name="Bob", country="USA")
# Output:
# a: 1
# b: 2
# args: (3, 4, 5)
# c: 20
# kwargs: {'name': 'Bob', 'country': 'USA'}
 
my_function(1,2)
# Output:
# a: 1
# b: 2
# args: ()
# c: 10
# kwargs: {}

# Use Cases
# Flexible Function Design: *args and **kwargs make your functions more flexible, allowing them to handle a varying number of inputs without needing to define a specific number of parameters.
# Decorator Implementation: Decorators often use *args and **kwargs to wrap functions that might have different signatures.
# Function Composition: You can use *args and **kwargs to pass arguments through multiple layers of function calls.
# Inheritance: Subclasses can accept extra parameters to those defined by parent classes.
# Example showing use in inheritance
class Animal:
  def __init__(self, name):
    self.name = name
 
class Dog(Animal):
  def __init__(self, name, breed, *args, **kwargs):
    super().__init__(name)
    self.breed = breed
    # Process any additional arguments or keyword arguments here
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
 
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador", 1,2,3, color="Black", age = 5)