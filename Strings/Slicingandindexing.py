# String slicing and indexing
# In Python, strings are sequences of characters, and each character has an index. You can access individual characters using indexing and extract substrings using slicing.


# String Indexing

# Str = "Python"
# print(Str[0]) #Prints the nth index character from a string  Syntax: Print(Var[n])

# String Slicing
# Slicing allows you to extract a portion of a string using the syntax string[start:stop:step].

# Str = "Hello, Python!"
# print(Str[0:8])     # Output: Hello, P
# print(Str[0:8:2])   # Output: Hlo

# Step Parameter
# The step parameter defines the interval of slicing.
text = "Python Programming"
print(text[::2])   # Output: Pto rgamn
# print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)

# Practical Uses of Slicing
# String slicing is useful in many scenarios:

# Extracting substrings
# Reversing strings
# Removing characters
# Manipulating text efficiently
# text = "Welcome to Python!"
# print(text[:7])   # Output: Welcome
# print(text[-7:])  # Output: Python!
# print(text[3:-3]) # Output: come to Pyt