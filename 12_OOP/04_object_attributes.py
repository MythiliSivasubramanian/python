"""
Object Attributes:
    1. Attributes are variables that belong to an object.
    2. Each object can have its own unique values.
    3. Attributes are usually defined inside a constructor method called __init__.

"""

# Define a class Dog
class Dog:
   # Attributes : name, age
   # __init__ runs automatically when object is created
   def __init__(self, name, age): 
       self.name = name # self refers to the specific object being created. 
       # self.name belongs to this object  and it is the attribute name of that object
       self.age = age  # self refers to the specific object being created. self.age belongs to this object
        

# Create objects outside the class
dog1 = Dog("Buddy",3)
dog2 = Dog("Rocky",5)
    
# Access object attributes
print(dog1.name,dog1.age)
print(dog2.name,dog2.age)

# Change an attribute of dog1
dog1.age = 10

print("\nAfter changing dog1's age:")
print(f"dog1 → Name: {dog1.name}, Age: {dog1.age}")
print(f"dog2 → Name: {dog2.name}, Age: {dog2.age}")  # dog2 remains unchanged


# Memory IDs 
print("\nObject IDs:")
print(f"dog1 ID: {id(dog1)}")
print(f"dog2 ID: {id(dog2)}")