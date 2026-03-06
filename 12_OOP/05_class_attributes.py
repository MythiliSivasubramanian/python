"""
05_class_attributes.py

Difference between class attributes and instance (object) attributes:

Key Concepts:
1. Class attributes are shared across all instances of a class.
2. Instance attributes belong to a specific object and can override class attributes.
3. Deleting an instance attribute reveals the class attribute again.
"""

# Example 1: Class vs Instance attributes
class Dog:
    species = "Canine"  # Class attribute shared by all Dog objects

# Creating objects
dog1 = Dog()  # Object 1
dog2 = Dog()  # Object 2

# Creating an instance attribute for dog1
dog1.species = "Fox"  # Overrides class attribute for dog1 only

# Accessing attributes
print(f"\n\ndog1.species: {dog1.species}")  # Fox (instance attribute)
print(f"\ndog2.species: {dog2.species}")  # Canine (class attribute)

# Changing class attribute
Dog.species = "Wolf"
print(f"\n\nChanging class attribute :\n\n")

# Accessing attributes after class change
print(f"dog1.species: {dog1.species}\n")  # Fox (instance attribute still overrides)
print(f"dog2.species: {dog2.species}\n\n")  # Wolf (class attribute now reflected)


# Example 2: Deleting instance attribute to reveal class attribute
class Dogs:
    species1 = "Canine"  # Class attribute

# Create object
dogs1 = Dogs()  

# Create instance attribute
dogs1.species1 = "Fox"

# Delete instance attribute
del dogs1.species1

# Access attribute
print(dogs1.species1)  # Canine (class attribute is now visible)