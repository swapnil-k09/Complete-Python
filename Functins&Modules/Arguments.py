# Function Arguments & Return Values
# Functions can take parameters and return values.

# Types of Arguments:

# Positional Arguments
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8

# Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!

# Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")
student(age=20, name="Bob")