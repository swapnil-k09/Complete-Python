# String Methods and Functions
#Python provides a variety of built-in string methods and functions to manipulate and process strings efficiently.
# Common String Methods
# # Changing Case
# a = "hello, world!"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())

# Removing Whitespace
# a = "   hello, world!   "
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# Finding and Replacing
# a = "Hello, World!"

# a  = a.replace("Hello", "Goodbye")
# print(a)
# or 
# print(a.replace("Hello", "Goodbye"))

# # Splitting and Joining
# text = "apple,banana,orange"
# fruits = text.split(",")
# print(fruits)  # Output: ['apple', 'banana', 'orange']

# new_text = " - ".join(fruits)
# print(new_text)  # Output: "apple - banana - orange"

# Checking String Properties
# a = "Hello"
# print(a.islower())
# print(a.isupper())
# print(a.isalpha())
# print(a.isalnum())

# Useful Built-in String Functions
# len() - Get Length of a String
# text = "Hello, Python!"
# print(len(text))  # Output: 14

# # ord() and chr() - Character Encoding
# print(ord('A'))  # Output: 65
# print(chr(65))   # Output: 'A'