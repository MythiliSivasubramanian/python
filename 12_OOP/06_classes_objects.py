"""
Class :     Blue print for objects. 
Objects :   Instance created from a class. Each object of the class has thier own indepedent memory and data.
                __init__ is a special function that runs automatically whenever an object is created.
                self refers that an object is being created.
Method :    A function defined inside a class 
                self gives the meothod the access to objects attributes.
                
Class Attributes vs Instance attributes:
    Instance attributes : belong to specific objects (self.name, self.age)
    Class attributes : belong to the class itself; all objects share it


# Define a class Dog
class Dog:
    species = "Canine"     # Class attributes, shared by all objects of class unless object has it own data
    # Defining and adding attributes 
    def __init__(self, name, age): # __init__ special method called automatically when an object is created
        # refers to the object being created (dog1 or dog2)
        self.name = name # store data in that object only
        self.age = age # store data in that object only
        
    # Define a function bark()
    def bark(self):   # self gives the method the access to objects that calls it.
        print(f"{self.name} says Woof!") # self.name accesses the name attribute of the specific object
        # always prints the name of the calling object
        
    
    def birthday(self):
        # Increase the age by 1
        self.age += 1
        print(
                f"Name : {self.name}\t\tAge : {self.age}"
             )
    
# Create Objects/instances (dog1) and dog2 of class Dog  with different names and ages
# Class is 1st defined and objects of the class are created outside class definition
dog1 = Dog("Lilly",4) 
dog2 = Dog("Tommy",6)

# Print Class & Objects and its type
# The class itself is an object of type type
print(
        f"\n\nClass : \n\tClass Name : Dog\n\tClass Type : {type(Dog)}\n\n"
        f"Objects : \n\tObject 1 : {dog1}\n\tObject Type : {type(dog1)}\n\n"
        f"\tObject 2 : {dog2}\n\tObject Type : {type(dog2)}\n\n"
    )

# Print each object’s name and age by accessing objects attributes
print(
        f"Print each object’s name and age :\n"
        f"Object 1 :\nName : {dog1.name}\tAge : {dog1.age}\n\n"
        f"Object 2 :\nName : {dog2.name}\tAge : {dog2.age}\n\n"    
    )

# Call method bark() for both objects dog1 and dog2
print(f"Calling bark() for both objects dog1 and dog2 :\n")
dog1.bark()
dog2.bark()


# Current details of dog1 and dog2
print(
        f"\n\nCurrent details :\nDog 1 : \tName : {dog1.name}\t\tAge : {dog1.age}\n"
        f"Dog 2 : \tName : {dog2.name}\t\tAge : {dog2.age}\n\n"
    )

# Call method birthday() for both objects dog1 and dog2
print(f"After thier Birthday :\n")
dog1.birthday()
dog2.birthday()

print(f"\n\nAccessing Class Attributes :\n")
print(
        f"Dog1.species : {dog1.species}\n"
        f"Dog2.species : {dog2.species}\n\n"
      )

dog1.species = "Wolf"
print("After changing dog1.species = 'Wolf' :\n")
print(
        f"Dog1.species : {dog1.species}\n"
        f"Dog2.species : {dog2.species}\n\n"
      )


"""

class Dog:
    tricks = []   # class attribute (mutable)

    def add_trick(self, trick):
        self.tricks.append(trick)


dog1 = Dog()
dog2 = Dog()

dog1.add_trick("roll over")
dog2.add_trick("play dead")

print(dog1.tricks)
print(dog2.tricks)