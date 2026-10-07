# 1. Defining Functions
# Write a function greet() that prints "Hello, Python Learner!" when called.
"""def greet():
    print("Hello, Python Learner!")
greet()"""

# Write a function square(num) that returns the square of a given number. Test it with different numbers.
"""def square(num):
    return num ** 2
num = int(input("Enter length of one side of square: "))
print(square(num))"""

# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
"""def full_name(first, last):
    print(f"{first} {last}")
full_name("John", "Doe")  # Example usage"""

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)
"""def area(length, width=10):
    print("Area of rectangle is:", length * width)
a = int(input("Enter length of rectangle: "))
b = int(input("Enter width of rectangle: "))
area(a, b)"""

# Write a lambda function that adds two numbers and test it.
"""add = lambda x,y : x + y
print(add(3,4))"""

# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
"""numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)"""

# Write a recursive function factorial(n) that returns the factorial of a number.
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))"""

# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
"""def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(1234))"""

# Import the math module and use it to:
"""import math
print(math.sqrt(144))
print(math.radians(90))"""

# install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
"""import requests
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Data fetched successfully!")
    print(response.json())"""

# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
"""counter = 0
def increment():
    global counter
    print("Counter value:", counter)
    counter += 1
increment()
increment()
increment()"""

# # Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
# def multiply(a, b):
#     """
#     This function takes two numbers as input and returns their product.
    
#     Parameters:
#     a (int or float): The first number.
#     b (int or float): The second number.
    
#     Returns:
#     int or float: The product of the two numbers.
#     """
#     print(a*b)
# help(multiply)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# multiply(a, b)

# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
"""def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
print(fibonacci(10))  # Example usage"""

# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
"""def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    else:
        return a / b

print(safe_divide(10, 2))  # Example usage
print(safe_divide(10, 0))  # Example usage"""

# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
"""from my_utils import is_even
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")"""