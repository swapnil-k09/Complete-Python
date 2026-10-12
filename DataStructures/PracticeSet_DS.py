# 1. Create a list fruits = ["apple", "banana", "cherry"].

# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.

"""fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "Orange"
print(fruits)
print(len(fruits))"""

# Create a list of numbers from 1 to 10.

# Print the first three numbers using slicing.
# Print the last three numbers using slicing.
"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0:3])
print(num[6:9])"""

# Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.

"""lst = [5, 2, 9, 1, 7]
print(sorted(lst))
print(lst)
lst.append(10)
print(lst)
lst.remove(2)
print(lst)"""

# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.
"""names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)"""

#  Tuples and Operations on Tuples
# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
"""coordinates = (10, 20)
# print((coordinates[0], coordinates[1]))
# coordinates[0] = 50
print((coordinates[0], coordinates[1]))
lst = list(coordinates)
print(lst)
lst[0] = 50
print(lst)
print(tuple(lst))"""

# Sets and Set Methods
# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
# Add 5 to the set, remove 2, and check if 4 is in the set.
# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# Find their:
# Union
# Intersection
# Difference (a - b)

"""my_set = {1, 2, 3, 3, 4}
print(my_set)
my_set.add(5)
my_set.remove(2)
print(4 in my_set)
print(my_set)"""

"""a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))"""

#  Dictionaries and Dictionary Methods
# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".

"""student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student["grade"])
student["city"] = "Delhi"
print(student)"""

# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them
"""dict = {"John": "123-456-7890", "Jane": "456-123-45678", "Jack": "789-456-123-4567"}
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())"""

# 6. Bonus Challenges
# Write a program that takes a list of numbers and removes all duplicates using a set.
# Given a dictionary of products and their prices, find the product with the highest price.
# Write a program that merges two dictionaries into one.

"""my_list = []
for i in range(5):
    value = int(input("Enter a number: "))
    my_list.append(value)
print("Final list:", my_list)
my_list.sort()
my_list = list(set(my_list))
print("after removing duplicates:", my_list)"""

"""products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 1500,
    "Keyboard": 800
}
print(products)
print(max(products.values()))"""


""dicta = {"a": 1, "b": 2, "c": 3}
dictb = {"d": 4, 'e': 5, 'f': 6}
# merge two dictionaries into one
dicta.update(dictb)
print(dicta)""