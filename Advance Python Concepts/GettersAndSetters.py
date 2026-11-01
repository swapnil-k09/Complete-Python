# Getters and Setters
# In object-oriented programming, getters and setters are methods used to control access to an object's attributes (also known as properties or instance variables). They provide a way to encapsulate the internal representation of an object, allowing you to validate data, enforce constraints, and perform other operations when an attribute is accessed or modified. While Python doesn't have private variables in the same way as languages like Java, the convention is to use a leading underscore (_) to indicate that an attribute is intended for internal use.

# Using getters and setters helps:

# Encapsulate data and enforce validation: You can check if the new value meets certain criteria before assigning it.
# Control access to "private" attributes: By convention, attributes starting with an underscore are considered private, and external code should use getters/setters instead of direct access.
# Make the code more maintainable: Changes to the internal representation of an object don't necessarily require changes to code that uses the object.
# Add additional logic: Logic can be added when getting or setting attributes.
# Using Getters and Setters
# Traditional Approach (Using Methods)
# A basic approach is to use explicit getter and setter methods:

class Person:
    def __init__(self, name):
        self._name = name  # Convention: underscore (_) denotes a private attribute.
 
    def get_name(self):
        return self._name
 
    def set_name(self, new_name):
        self._name = new_name 
 
p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob 

# Using @property (Pythonic Approach)
# Python provides a more elegant and concise way to implement getters and setters using the @property decorator. This allows you to access and modify attributes using the usual dot notation (e.g., p.name) while still having the benefits of getter and setter methods.

class Person:
    def __init__(self, name):
        self._name = name
 
    @property
    def name(self):  # Getter
        return self._name
 
    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 
 
p = Person("Alice")
print(p.name)  # Alice (calls the getter)
 
p.name = "Bob"  # Calls the setter
print(p.name)  # Bob
 

# Benefits of @property:
# Attribute-like access: You can use obj.name instead of obj.get_name() and obj.set_name(), making the code cleaner and more readable.

# Consistent interface: The external interface of your class remains consistent even if you later decide to add validation or other logic to the getter or setter.

# Read-only properties: You can create read-only properties by simply omitting the @property.setter method (see the next section).

# @property.deleter: deletes a property. Here is an example:

class Person:
    def __init__(self, name):
        self._name = name
 
    @property
    def name(self):  # Getter
        return self._name
 
    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 
 
    @name.deleter
    def name(self):
        del self._name
 
p = Person("Alice")
print(p.name)  # Alice
del p.name
print(p.name)  # AttributeError: 'Person' object has no attribute '_name'

# Read-Only Properties
# If you want an attribute to be read-only, define only the @property decorator (the getter) and omit the @name.setter method. Attempting to set the attribute will then raise an AttributeError.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius 
    @property
    def area(self):  # Read-only computed property
        return 3.1416 * self._radius * self._radius
c = Circle(5)
print(c.radius)  # 5
print(c.area)  # 78.54
 
# c.radius = 10  # Raises AttributeError: can't set attribute
# c.area = 20 # Raises AttributeError: can't set attribute

# Recap
# Getters and Setters provide controlled access to an object's attributes, promoting encapsulation and data validation.
# The @property decorator offers a cleaner and more Pythonic way to implement getters and setters, allowing attribute-like access.
# You can create read-only properties by defining only a getter (using @property without a corresponding @<attribute>.setter).
# Using @property, you can dynamically compute values (like the area in the Circle example) while maintaining an attribute-like syntax.



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        a = self.name.split(" ")
        return a[0]
    @first_name.setter
    def first_name(self, name2):
        l = self.name.split(" ")
        new_name = f"{name2} {l[1]}"
        self.name = new_name
E1 = Employee("Swapnil Kadam", "100000")
print(E1.first_name)
E1.first_name = "Swappy"
print(E1.first_name)
print(E1.name)