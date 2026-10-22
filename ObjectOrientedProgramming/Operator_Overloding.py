# Method Overriding and Operator Overloading
# Method Overriding: Customizing Inherited Behavior
# Method overriding is how polymorphism is achieved in inheritance. When a child class defines a method with the same name as a method in its parent class, the child's version overrides the parent's version for objects of the child class. This allows specialized behavior in subclasses. The parent class's method is still available (using super()), but when you call the method on a child class object, the child's version is executed.

# Operator Overloading: Making Operators Work with Your Objects
# Python lets you define how standard operators (like +, -, ==) behave when used with objects of your own classes. This is done using special methods called "magic methods" (or "dunder methods" because they have double underscores before and after the name).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y  
 
    def __add__(self, other):  # Overloading the + operator
        #  'other' refers to the object on the *right* side of the +
        return Point(self.x + other.x, self.y + other.y)
 
    def __str__(self): # String representation (for print() and str())
        return f"({self.x}, {self.y})"
 
    def __eq__(self, other): # Overloading == operator
        return self.x == other.x and self.y == other.y
 
p1 = Point(1, 2)
p2 = Point(3, 4)
 
p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)
print(p3)      # Output: (4, 6)  (This uses the __str__ method)
 
print(p1 == p2) # Output: False (This uses the __eq__ method)

# Other useful magic methods: (You don't need to memorize them all, but be aware they exist!)

# __sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __len__ (len()), __getitem__, __setitem__, __delitem__ (for list/dictionary-like behavior – allowing you to use [] with your objects).
# Getters and Setters: Controlling Access to Attributes
# Getters and setters are methods that you create to control how attributes of your class are accessed and modified. They are a key part of the principle of encapsulation. Instead of directly accessing an attribute (like my_object.attribute), you use methods to get and set its value. This might seem like extra work, but it provides significant advantages.

# Why use them?

# Validation: You can add checks within the setter to make sure the attribute is set to a valid value. For example, you could prevent an age from being negative.
# Read-Only Attributes: You can create a getter without a setter, making the attribute effectively read-only from outside the class. This protects the attribute from being changed accidentally.
# Side Effects: You can perform other actions when an attribute is accessed or modified. For instance, you could update a display or log a change whenever a value is set.
# Maintainability and Flexibility: If you decide to change how an attribute is stored internally (maybe you switch from storing degrees Celsius to Fahrenheit), you only need to update the getter and setter methods. You don't need to change every other part of your code that uses the attribute. This makes your code much easier to maintain and modify in the future.
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Convention: _age indicates it's intended to be "private"
 
    def get_age(self):  # Getter for age
        return self._age
 
    def set_age(self, new_age):  # Setter for age
        if new_age >= 0 and new_age <= 150:  # Validation
            self._age = new_age
        else:
            print("Invalid age!")
 
person = Person("Alice", 30)
print(person.get_age())  # Output: 30
 
person.set_age(35)
print(person.get_age())  # Output: 35
 
person.set_age(-5)   # Output: Invalid age!
print(person.get_age())   # Output: 35 (age wasn't changed)

# The Pythonic Way: @property Decorator

# Python offers a more elegant and concise way to define getters and setters using the @property decorator. This is the preferred way to implement them in modern Python.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Convention: _age for "private" attributes
 
    @property  # This makes 'age' a property (the getter)
    def age(self):
        return self._age
 
    @age.setter # This defines the setter for the 'age' property
    def age(self, new_age):
        if new_age >= 0 and new_age <= 150:
            self._age = new_age
        else:
            print("Invalid age!")
 
person = Person("Bob", 40)
print(person.age)    # Output: 40  (Looks like direct attribute access, but calls the getter)
person.age = 45      # (Calls the setter – looks like attribute assignment)
print(person.age)
person.age = -22 #Output: Invalid age!

# With @property, accessing and setting the age attribute looks like you're working directly with a regular attribute, but you're actually using the getter and setter methods behind the scenes. This combines the convenience of direct access with the control and protection of encapsulation.

# Private Variables (and the _ convention):

# It's important to understand that Python does not have truly private attributes in the same way that languages like Java or C++ do. There's no keyword that completely prevents access to an attribute from outside the class.

# Instead, Python uses a convention: An attribute name starting with a single underscore (_) signals to other programmers that this attribute is intended for internal use within the class. It's a strong suggestion: "Don't access this directly from outside the class; use the provided getters and setters instead." It's like a "Please Do Not Touch" sign.

class MyClass:
    def __init__(self):
        self._internal_value = 0  #  Convention: _ means "private"
 
    def get_value(self):
        return self._internal_value
 
obj = MyClass()
# print(obj._internal_value)  # This *works*, but it's against convention
print(obj.get_value())       # This is the preferred way

# While you can still access obj._internal_value directly, doing so is considered bad practice and can lead to problems if the internal implementation of the class changes. Always respect the underscore convention! It's about good coding style and collaboration.


"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def prints(self):
        print(self.x, self.y)
p1 = Point(2, 3)
p2 = Point(4, 5)
other = p1.sum(p2)
other.prints()
"""