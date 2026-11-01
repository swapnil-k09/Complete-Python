# Exception Handling and Custom Errors
# Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. Python provides a robust mechanism for handling exceptions using try-except blocks. This allows your program to gracefully recover from errors or unexpected situations, preventing crashes and providing informative error messages. You can also define your own custom exceptions to represent specific error conditions in your application.

# Basic Exception Handling
# The try-except block is the fundamental construct for handling exceptions:

# The try block contains the code that might raise an exception.
# The except block contains the code that will be executed if a specific exception occurs within the try block.
"""try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")"""

# Output:
# Cannot divide by zero!
# Handling Multiple Exceptions
# You can handle multiple types of exceptions using multiple except blocks or by specifying a tuple of exception types in a single except block.

"""try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
 
# Alternative using a tuple:
try:
  num = int(input("Enter a number: "))
  result = 10 / num
except (ZeroDivisionError, ValueError) as e:
  print(f"An error occurred: {e}")"""

# Using else and finally
# else: The else block is optional and is executed only if no exception occurs within the try block. It's useful for code that should run only when the try block succeeds.
# finally: The finally block is also optional and is always executed, regardless of whether an exception occurred or not. It's typically used for cleanup operations, such as closing files or releasing resources.
"""try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
    print(f"File contents:\n{content}")
finally:
    file.close()  # Ensures the file is closed no matter what"""

# Raising Exceptions (raise)
# You can manually raise exceptions using the raise keyword. This is useful for signaling error conditions in your own code.

"""def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."
 
try:
  print(check_age(20))  # Access granted.
  print(check_age(16))  # Raises ValueError
except ValueError as e:
  print(f"Error: {e}")
"""
# Custom Exceptions
# Python allows you to define your own custom exception classes by creating a new class that inherits (directly or indirectly) from the built-in Exception class (or one of its subclasses). This makes your error handling more specific and informative.

"""class InvalidAgeError(Exception):
    """"""Custom exception for invalid age.""""""
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)
 
def verify_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise your custom exception
    return "Welcome!"
 
try:
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")
"""
# By defining custom exceptions, you can:

# Create a hierarchy of exceptions that reflect the specific error conditions in your application.
# Provide more informative error messages tailored to your application's needs.
# Make it easier for other parts of your code (or other developers) to handle specific errors appropriately.
# Conclusion
# try-except blocks are essential for handling errors and preventing program crashes.
# Multiple except blocks or a tuple of exception types can be used to handle different kinds of errors.
# The else block executes only if no exception occurs in the try block.
# The finally block always executes, making it suitable for cleanup tasks.
# The raise keyword allows you to manually trigger exceptions.
# Custom exceptions (subclasses of Exception) provide a way to represent application-specific errors and improve error handling clarity.


"""while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number:"))
        print(f"Sum of two numbers is: {a + b}")
    except Exception as e:
        print("Invalid input! Please enter a number.", e)"""


# Raising an Error:

"""a = int(input("Enter your age:"))
try:
    if a < 18:
        raise ValueError("Age must be 18 or older!")
except Exception as e:
    print(e)
else:
    print("Age: ", a)  # Or at between line 109 and line 110.
finally:
    print("Thank You!")
"""