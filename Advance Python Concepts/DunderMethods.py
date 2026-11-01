# Magic/Dunder Methods
# Magic methods, also called dunder (double underscore) methods, are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__, __add__). These methods allow you to define how your objects interact with built-in Python operators, functions, and language constructs. They provide a way to implement operator overloading and customize the behavior of your classes in a Pythonic way.

# They are used to:

# Customize object creation and initialization (__init__, __new__).
# Enable operator overloading (e.g., +, -, *, ==, <, >).
# Provide string representations of objects (__str__, __repr__).
# Control attribute access (__getattr__, __setattr__, __delattr__).
# Make objects callable (__call__).
# Implement container-like behavior (__len__, __getitem__, __setitem__, __delitem__, __contains__).
# Support with context managers (__enter__,__exit__)
# Common Magic Methods
# 1. __init__ – Object Initialization
# The __init__ method is the constructor. It's called automatically when a new instance of a class is created. It's used to initialize the object's attributes.

"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
p = Person("Alice", 30)
print(p.name, p.age)"""  # Alice 30

# 2. __str__ and __repr__ – String Representation
# __str__: This method should return a human-readable, informal string representation of the object. It's used by the str() function and by print().
# __repr__: This method should return an unambiguous, official string representation of the object. Ideally, this string should be a valid Python expression that could be used to recreate the object. It's used by the repr() function and in the interactive interpreter when you just type the object's name and press Enter.
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __str__(self):
        return f"Person({self.name}, {self.age})"  # User-friendly
 
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"  # Unambiguous, for debugging
 
p = Person("Alice", 30)
print(str(p))    # Person(Alice, 30)
print(repr(p))   # Person(name='Alice', age=30)
print(p)"""          # Person(Alice, 30)  # print() uses __str__ if available

# If __str__ is not defined, Python will use __repr__ as a fallback for str() and print(). It's good practice to define at least __repr__ for every class you create.

# 3. __len__ – Define Behavior for len()
# This method allows objects of your class to work with the built-in len() function. It should return the "length" of the object (however you define that).

"""class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
 
    def __len__(self):
        return self.pages
 
b = Book("Python 101", 250)
print(len(b))  # 250"""

# 4. __add__, __sub__, __mul__, etc. – Operator Overloading
# These methods allow you to define how your objects behave with standard arithmetic and comparison operators.

"""class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
 
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
      return Vector(self.x * scalar, self.y * scalar)
 
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
 
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__
print(v3)    # Vector(6, 8)
v4 = v3 - v1
print(v4)      # Vector(4, 5)
v5 = v1 * 5
print(v5) # Vector(10, 15)"""

# Other common operator overloading methods include:

# __eq__ (==)
# __ne__ (!=)
# __lt__ (<)
# __gt__ (>)
# __le__ (<=)
# __ge__ (>=)
# __truediv__ (/)
# __floordiv__ (//)
# __mod__ (%)
# __pow__ (**)
# Recap
# Magic (dunder) methods are a powerful feature of Python that allows you to:

# Customize how your objects interact with built-in operators and functions.
# Make your code more intuitive and readable by using familiar Python syntax.
# Implement operator overloading, container-like behavior, and other advanced features.
# Define string representation.

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"The name is: {self.name} and salary is: {self.salary}"
    def __repr__(self):
        return f"name:{self.name}\nsalary:{self.salary}"
    def __len__(self):
        return len(self.name)

e = Employee("Swapnil", 50000)
print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e))