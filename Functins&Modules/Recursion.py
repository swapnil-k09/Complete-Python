# Recursion in Python
# A function calling itself to solve a problem.
# Recursion in Python is a programming technique where a function calls itself to solve a smaller instance of the same problem. It allows you to break down complex tasks into repeatable, self-similar steps.
# Syntax:

"""
def recursive_function(parameters):
    # 1. Base Case: The stopping condition
    if condition_to_stop:
        return base_value
    
    # 2. Recursive Case: The function calls itself
    else:
        # Arguments must change to move closer to the base case
        return recursive_function(modified_parameters)
"""

# Example: Factorial using Recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
 
# print(factorial(5))  # Output: 120

# # Eg.2: Sum upto the nummber n using Recursion
# def sum_n (n):
#     if n == 0:
#         return 0
#     return n + sum_n(n-1)
# print(sum_n(5))  # Output: 15

# Important Notes:
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.