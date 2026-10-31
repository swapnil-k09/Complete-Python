"""1. Create a Simple Class and Object
Create a class Car with a method drive() that prints "Car is moving".
Create an object of Car and call drive()."""

# class car:
#     def __init__(self):
#         pass
#     def drive(self):
#         print("Car is moving.")
# car1 = car()
# car1.drive()


"""2. Constructor and Attributes
Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person’s name and age."""


# class person:
#     def __init__(self):
#         a = input("Enter your name: ")
#         b = int(input("Enter your age: "))
#         self.name = a
#         self.age = b
#     def p_data(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# per1 = person()
# per1.p_data()

"""3. Simple Inheritance
Create a base class Animal with a method sound() that prints "Some sound".
Create a derived class Dog that overrides sound() to print "Bark!".
Create an object of Dog and call sound()."""

# class animal:
#     def __init__(self, name):
#         self.name = name
#     def sound(self):
#         print(f"{self.name} is making some sound.")
# class  dog(animal):
#     def  sound(self):
#         print("Bark!")
# d = dog("Orry")
# d.sound()