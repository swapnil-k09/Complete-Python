# Tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined by enclosing the elements in parentheses `()`.
# Eg:
t1 = (12, 13, 12, 14, 15)
t2 = (12, 13, 14, 15)
print(t1)  # Outputs: (12, 13, 14, 15)
# Slicing
print(t1[0:2]) # Outputs: (12, 13) - Slicing the tuple to get the first two elements
# Tuple with only one element is called a singleton tuple.
# Eg: t1 = (12,) - A singleton tuple.

# Touple Unpacking

t3 = (1, 2, 3)
print("t3:",t3)
a, b, c =t3
print(a)

# Touple Methods:
# 1. t1.count(12) - Returns the number of times the element 12 occurs in the tuple.
print(t1.count(12))
# 2. t1.index(12) - Returns the index of the first occurrence of the element 12 in the tuple.
print(t1.index(12))
# 3. t1.index(12, 2) - Returns the index of the first occurrence of the element 12 in the tuple starting from the index 2.
print(t1.index(12, 2))
# 4. t1.index(12, 2, 5) - Returns the index of the first occurrence of the element 12 in the tuple starting from the index 2 and ending at the index 5.
print(t1.index(12, 2, 5))