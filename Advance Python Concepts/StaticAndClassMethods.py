# Static & Class Methods
# In Python, methods within a class can be of three main types:

# Instance Methods: These are the most common type of method. They operate on instances of the class (objects) and have access to the instance's data through the self parameter.
# Class Methods: These methods are bound to the class itself, not to any particular instance. They have access to class-level attributes and can be used to modify the class state. They receive the class itself (conventionally named cls) as the first argument.
# Static Methods: These methods are associated with the class, but they don't have access to either the instance (self) or the class (cls). They are essentially regular functions that are logically grouped within a class for organizational purposes.
# Instance Methods (Default Behavior)
# Instance methods are the default type of method in Python classes. They require an instance of the class to be called, and they automatically receive the instance as the first argument (self).

class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute
 
    def speak(self):
        return f"{self.name} says Woof!"
 
dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!

# Class Methods (@classmethod)
# A class method is marked with the @classmethod decorator. It takes the class itself (cls) as its first parameter, rather than the instance (self). Class methods are often used for:

# Modifying class attributes: They can change the state of the class, which affects all instances of the class.
# Factory methods: They can be used as alternative constructors to create instances of the class in different ways.
class Animal:
    species = "Mammal"  # Class attribute
 
    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modifies class attribute
 
    @classmethod
    def get_species(cls):
        return cls.species
 
print(Animal.get_species())  # Mammal
Animal.set_species("Reptile")
print(Animal.get_species())  # Reptile
 
# You can also call class methods on instances, but it's less common:
a = Animal()
print(a.get_species()) # Reptile

# Example: Alternative Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))  # Creates a new Person instance
 
p = Person.from_string("Alice-30")
print(p.name, p.age)  # Alice 30

# In this example, from_string acts as a factory method, providing an alternative way to create Person objects from a string.

# Static Methods (@staticmethod)
# Static methods are marked with the @staticmethod decorator. They are similar to regular functions, except they are defined within the scope of a class.

# They don't take self or cls as parameters.
# They are useful when a method is logically related to a class but doesn't need to access or modify the instance or class state.
# Often used for utility functions that are related to the class
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
 
print(MathUtils.add(3, 5))  # 8
 
#Can also be called on an instance
m = MathUtils()
print(m.add(4,5)) # 9

# When to Use Static Methods?
# When a method is logically related to a class but doesn't require access to instance-specific or class-specific data.
# For utility functions that perform operations related to the class's purpose (e.g., mathematical calculations, string formatting, validation checks).