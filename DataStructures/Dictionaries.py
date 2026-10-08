# Dictionaries and Dictionary Methods
# Dictionaries store key-value pairs and allow fast lookups.

# Creating a Dictionary:
student = {"name": "Alice", "age": 21, "grade": "A"}

# Accessing & Modifying Values:
print(student["name"])  # Output: Alice
student["age"] = 22     # Updating value
student["city"] = "New York"  # Adding new key-value pair

# Common Dictionary Methods:
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # dict_values(['Alice', 22, 'A', 'New York'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ...])
 
student.pop("age")  # Removes "age" key
student.clear()  # Empties dictionary

# Dictionary Comprehensions:
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}