# # Practice Set

# Q1. Basic String Operations
# # Create a string variable name with your full name. Print:
"""
name = "Swapnil Patil"
print(name[0:1])  # First character
print(name[-1])  # Last character
print(len(name))  # Length of the string
"""

# # Concatenate two strings: "Hello" and "World" with a space in between.
"""
a = "Hello"
b = "World"
print(f"{a}, {b}!")
"""


# Q2. String Slicing and Indexing
"""
text = "Python Programming"
# Print the first 6 characters
print(text[0:6])  # Output: Python
#Print the last 6 characters
print(text[-6:])  # Output: mming
# Print every second character
print(text[::2])  # Output: Pto rgamn
# reverse the string using slicing
print(text[::-1])  # Output: gnimmargorP nohtyP
"""


# Q3 String Methods and Functions
"""
Q3 = "  i love python programming  "
print(q3.strip())  # Output: i love python programming
print(q3.title())  # Output: I Love Python Programming
#find how many times 'o' is present in the string
print(q3.count('o'))  # Output: 3
"""

# x3 = "123abc"
# print(x3.isalnum())  # Output: True


# Q4. String Formatting and f-Strings
"""
a = "John"
b = 25
print("My name is {} and I am {} years old.".format(a, b))  # Using .format() for formatting
print(f"My name is {a} and I am {b} years old.")  # Using f-strings for formatting
"""


# Q5. String Manipulation Challenges
"""
sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"))  # Output: Coding in Python is awesome
print(sentence.find("Python"))  # Output: 10
print(sentence.upper())  # Output: CODING IN PYTHON IS FUN
"""


# Q6. Write a program that counts how many vowels are in a given string.
"""
vowels = "aeiouAEIOU"
a = input("Enter a string: ")
count = 0
for char in a:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")
"""

# Take a user input string and check if it is a palindrome
"""
string = input("Enter a string: ")
cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.") #eg: input: "A man, a plan, a canal: Panama" -> Output: The string is a palindrome.
"""
