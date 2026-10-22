# Constructors in Python
# The Constructor: Setting Things Up (__init__)
# The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

# What's it for? The constructor's job is to initialize the object's attributes – to give them their starting values. It sets up the initial state of the object.

class Dog:
    def __init__(self, name, breed):  # The constructor
        self.name = name      # Setting the name attribute
        self.breed = breed    # Setting the breed attribute
 
# When we do this:
my_dog = Dog("Fido", "Poodle")  # The __init__ method is automatically called
 
# It's like we're saying:
# 1. Create a new Dog object.
# 2. Run the __init__ method on this new object:
#    - Set my_dog.name to "Fido"
#    - Set my_dog.breed to "Poodle"

# You can also set default values for parameters in the constructor, making them optional when creating an object:

class Dog:
    def __init__(self, name="Unknown", breed="Mixed"):
        self.name = name
        self.breed = breed
 
dog1 = Dog()          # name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rex")     # name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be "Labrador"





# Stock at the Store
class Stock:

    def __init__(self , name, qty, price):
        self.name = name
        self.qty  = qty
        self.price = price

    def get_Stock(self):
        return f"Name:{self.name}, {self.qty} left and price is {self.price}"

S1  = Stock("Apple", 10, 2.99)
print(S1.get_Stock())