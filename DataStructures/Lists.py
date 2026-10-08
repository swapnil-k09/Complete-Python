# Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Eg:

# a = ["apple", "banana", "cherry"]
b = [1, 5, 7, 9, 3]
# c = [True, False, False]
# d = ["abc", 34, True, 40, "male"]

# print(a)
# print(b)
# print(c)
# print(d)

# Slicing
# print(b[2:4])  # Outputs: cherry

# Common list methods:
# 1. append() - Adds an element at the end of the list
b.append(6)
print(b)  # Outputs: [1, 5, 7, 9, 3, 6]
# 2. insert() - Adds an element at the specified position
b.insert(2, 8)  # Inserts 8 at index 2 in the list b.
print(b)  # Outputs: [1, 5, 8, 7, 9, 3, 6]
# 3. remove() - Removes the first item with the specified value 
b.remove(5)  # Removes the first occurrence of 5 from the list b.
print(b)  # Outputs: [1, 8, 7, 9, 3, 6]
# 4. pop() - Removes the element at the specified position
b.pop(3)  # Removes the element at index 3 (which is 9) from the list b.
print(b)  # Outputs: [1, 8, 7, 3, 6]
# 5. clear() - Removes all the elements from the list
b.clear()  # Clears all elements from the list b.
print(b)  # Outputs: []
# 6. index() - Returns the index of the first element with the specified value
b = [1, 5, 7, 9, 3, 6]
print(b.index(7))  # Outputs: 2 (the index of the first occurrence of 7 in the list b)
# 7. count() - Returns the number of elements with the specified value
print(b.count(1))  # Outputs: 1 (the number of occurrences of 1 in the list b)
# 8. sort() - Sorts the list
b.sort()  # Sorts the list b in ascending order.
print(b)  # Outputs: [1, 3, 5, 6, 7, 9]
# 9. reverse() - Reverses the order of the list
b.reverse()  # Reverses the order of the list b.
print(b)  # Outputs: [9, 7, 6, 5, 3, 1]
# 10. copy()
# Returns a shallow copy of the list.
c = b.copy()  # Creates a shallow copy of the list b and assigns it to list c.
print(c)  # Outputs: [9, 7, 6, 5, 3, 1]



# List Comprehensions (Efficient List Creation)

Sq = [x**2 for x in range(10)]  # Creates a list of squares of numbers from 0 to 9.
print(Sq)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]