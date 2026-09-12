# Lambda Functions in Python
# Lambda functions are anonymous, inline functions.

# Syntax:
square = lambda x: x * x
print(square(4))  # Output: 16

# Example:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]