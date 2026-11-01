# Map filter and reduce
# map, filter, and reduce are higher-order functions in Python (and many other programming languages) that operate on iterables (lists, tuples, etc.). They provide a concise and functional way to perform common operations on sequences of data without using explicit loops. While they were more central to Python's functional programming style in earlier versions, list comprehensions and generator expressions often provide a more readable alternative in modern Python.

# Map
# The map() function applies a given function to each item of an iterable and returns an iterator that yields the results.

# Syntax: map(function, iterable, ...)

# function: The function to apply to each item.
# iterable: The iterable (e.g., list, tuple) whose items will be processed.
# ...: map can take multiple iterables. The function must take the same number of arguments

numbers = [1, 2, 3, 4, 5]
# Square each number using map
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
 
#Example with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed)) # Output: [5, 7, 9]
 
 
# Equivalent list comprehension:
squared_numbers_lc = [x**2 for x in numbers]
print(squared_numbers_lc)  # Output: [1, 4, 9, 16, 25]

# Filter
# The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.

# Syntax: filter(function, iterable)

# function: A function that returns True or False for each item. If None is passed, it defaults to checking if the element is True (truthy value).
# iterable: The iterable to be filtered.
# numbers = [1, 2, 3, 4, 5, 6]
 
# Get even numbers using filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]
 
# Equivalent list comprehension:
even_numbers_lc = [x for x in numbers if x % 2 == 0]
print(even_numbers_lc) # Output: [2, 4, 6]
 
# Example with None as function
values = [0, 1, [], "hello", "", None, True, False]
truthy_values = filter(None, values)
print(list(truthy_values)) # Output: [1, 'hello', True]

# Reduce
# The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.

# Syntax: reduce(function, iterable[, initializer])

# function: A function that takes two arguments.
# iterable: The iterable to be reduced.
# initializer (optional): If provided, it's placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.
from functools import reduce
 
numbers = [1, 2, 3, 4, 5]
 
# Calculate the sum of all numbers using reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
 
# Calculate the product of all numbers using reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120
 
#reduce with initializer
empty_list_sum = reduce(lambda x,y: x+y, [], 0)
print(empty_list_sum) # 0
 
# Without the initializer:
# empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError
 
# Equivalent using a loop (for sum):
total = 0
for x in numbers:
    total += x
print(total)  # 15

# When to use map, filter, reduce vs. list comprehensions/generator expressions:

# Readability: List comprehensions and generator expressions are often more readable and easier to understand, especially for simple operations.

# Performance: In many cases, list comprehensions/generator expressions can be slightly faster than map and filter.

# Complex Operations: reduce can be useful for more complex aggregations where

# Complex Operations: reduce can be useful for more complex aggregations where the logic is not easily expressed in a list comprehension. map and filter may also be preferable when you already have a named function that you want to apply.

# Functional Programming Style: If you're working in a more functional programming style, map, filter, and reduce can fit naturally into your code.