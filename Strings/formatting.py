# String formatting and f-strings

# String formatting
# String formatting is used for insert variables and expressions into strings in a structured way. Python provides multiple ways to format strings, including the older .format() method and the modern f-strings.

# a = "Alice"
# b = 30

# print("Hello, My name is {}. and I'm {} years old.".format(a, b))
# Yoy can also specify positions
# print("Hello, My name is {1}. and I'am {0} years old.".format(30, "Alice"))
# # instead of this, we can use f-strings.

# print(f"Hello, My name is {a}. and I'am {b} years old.")

# Using Expressions in f-Strings
# You can perform calculations directly inside f-strings:

# x = 10
# y = 5
# print(f"The sum of {x} and {y} is {x + y}")

# Formatting Numbers
# pi = 3.14159265
# print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Padding and Alignment
# text = "Python"
# print(f"{text:>10}")  # Right align
# print(f"{text:<10}")  # Left align
# print(f"{text:^10}")  # Center align