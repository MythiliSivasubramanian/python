"""
Methods:
    1. A method is a function defined inside a class. It can act on object’s data
    2. It can use the object’s attributes (via self) to perform actions.
    3. Its like behaviours of the object
    
    Attribute is the data inside object and it can be used or changed by methods
    
    Example class Dog:
    Concept	                Real-world example
    Attribute	            Name, Age
    Method	                Bark, Eat, Sleep
    
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self): # refers to the object calling the method
        print(f"\n{self.name} is barking now!\n")
        
# Create objects
dog1 = Dog("Buddy",3)
dog2 = Dog("Rocky", 5)

# Using Methods
dog1.bark() # Both objects use the same method but the output depends on the object’s own attributes
dog2.bark() # Both objects use the same method but the output depends on the object’s own attributes
dog1.bark()

# Example 2

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    # Adding method
    def show_info(self):
        print(f"\n\nBrand : {self.brand}\nYear : {self.year}")
    
    
# Create Objects
car1 = Car("BMW", 2020)
car2 = Car("Tesla",2025)

# Using / calling the methods
car1.show_info()
car2.show_info()