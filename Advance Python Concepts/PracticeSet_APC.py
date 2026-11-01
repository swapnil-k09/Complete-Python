# 1. Decorators in Python
# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".

"""def decorator(function):
    def wrapper():
        print("fuction is being called...")
        function()
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()"""

# Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
"""import time
def decorator(function):
    def wrapper():
        print("fuction is being called...")
        start = time.time()
        function()
        end = time.time()
        print(f"Function took {end-start} seconds to execute")
    return wrapper
@decorator
def sum():
    total = 0
    print("Counting...")
    for i in range (1, 1000001):
        total += i
    print("Sum:", total)

sum()"""

# 2. Getters and Setters
# Create a class Employee with a private attribute _salary.

# Use @property to define a getter for salary.
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.

"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Warning")
        else:
            self._salary = value

e = Employee("Swapnil", 70000)
print("current Salary: ", e.salary)

e.salary = 80000
print("Positive Salary: ", e.salary)

e.salary = -80000
print("NEgative Salary: ", e.salary)"""

# 3. Static & Class Methods
# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."
# Call both methods without creating an object.

"""class Mathutils:
    @staticmethod
    def add(a, b):
        return a+b
    @classmethod
    def description(cls):
        print(f"This is a utility class for math operations.")

print(Mathutils.add(12, 123))
Mathutils.description()"""

#  Magic/Dunder Methods
# Create a class Book with attributes title and author.

# Implement __str__() so that printing the object displays "Title by Author".
# Implement __len__() so that len(book) returns the length of the title.


"""class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Name is {self.title} and its written by {self.author}."
    def __len__(self):
        return len(self.title)
# Create two Book objects and test these methods.
a = book("Prem", "Swapnil")
b = book("Shyaam Chi Aai", "Sane Guruji")
print(a, b)
print(len(a), len(b))"""

# 5. Exception Handling and Custom Errors
# Write a program that asks the user to enter a number and handles:

# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

"""class NegativeNumberError(Exception):
    pass
try:
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a first number: "))
    if num2 < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    result = 100 / num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except NegativeNumberError as e:
    print("Error:", e)"""

# map(), filter(), and reduce()
# Use map() to convert [1, 2, 3, 4, 5] into their cubes.
# Use filter() to get only even numbers from [10, 11, 12, 13, 14].
# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].
"""
a = [1, 2, 3, 4, 5]
cubes = map(lambda x: x**x, a)
print(list(cubes))"""

"""a = [10, 11, 12, 13, 14]
even = filter(lambda x: x%2 == 0, a)
print(list(even))"""

#  Walrus Operator
# Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.
# Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.

"""while (text := input("Enter something: ")) != "quit":
    print("You entered:", text)
print("Program terminated!")"""


"""words = ["python", "rocks", "ai"]
lengths = [n for word in words if (n := len(word)) >= 4]
print(lengths)"""

# 8. *args and **kwargs
# Write a function sum_all(*args) that accepts any number of integers and returns their sum.
# Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
"""
   print_details(name="Alice", age=25, city="Delhi")
   # Output:
   # name: Alice
   # age: 25
   # city: Delhi"""


"""def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sum_all(10, 20, 30, 40, 50))
print(sum_all(5, 10))"""


"""def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=25, city="Delhi")"""

# 9. Bonus Challenges
# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
# Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
# Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.

"""def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started!")
        result = func(*args, **kwargs)
        print("Function completed!")
        return result
    return wrapper
@my_decorator
def add(a, b):
    return a + b
@my_decorator
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
print("Sum:", add(10, 20))
greet("Swapnil", 21)"""


"""class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def display(self):
        print(f"Vector: ({self.x}, {self.y})")
v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2
v1.display()
v2.display()
v3.display()"""


"""import logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)
class InvalidInputError(Exception):
    pass
while True:
    try:
        num = input("Enter a positive number (or quit): ")
        if num.lower() == "quit":
            break
        num = int(num)
        if num <= 0:
            raise InvalidInputError("Number must be positive!")
        print("Square:", num ** 2)
    except ValueError:
        logging.error("Invalid input! Please enter an integer.")
    except InvalidInputError as e:
        logging.error(e)
print("Program terminated successfully!")"""