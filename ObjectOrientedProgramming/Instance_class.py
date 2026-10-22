# Instance and class attributes
# Class vs. Instance Attributes:
# Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.

# Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.A

class Stock:
    Not_Avbl = "Store is Closed!"     # This is Class Attribute.(Printed if instance attribute is'nt mentioned)
    def __init__(self , name, qty, price):
        self.name = name
        self.qty  = qty
        self.price = price

    def get_Stock(self):
        return f"Name:{self.name}, {self.qty} left and price is {self.price}"

S1  = Stock("Apple", 10, 2.99)
print(S1.get_Stock())

# Object introspection
print(dir(S1))
print(Stock.Not_Avbl)