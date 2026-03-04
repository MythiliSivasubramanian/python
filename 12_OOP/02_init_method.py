"""
 __init__ constructor in Python classes: 

__init__ runs automatically when an object is created and is commonly used
to initialize instance attributes.

"""

class Person:
 #  Represents a person with basic profile details

    def __init__(self, name, age, country, languages):
       # Initialize a person with name, age, country, and spoken languages
        self.name = name
        self.age = age
        self.country = country
        self.languages = languages
    
# Create objects p1 and p2 for class Person
p1 = Person("Anderson", 22, "Norway", ["English", "Spanish", "Chinese"])
p2 = Person("Ava", 25, "Canada", ["English", "French"])

print(
    f"\n\nDetails of Person 1 : \n\n"
    f"Name : {p1.name}\n"
    f"Age : {p1.age}\n"
    f"Country : {p1.country}\n"
    f"Languages : {p1.languages}\n\n"
)

print(
    f"Details of Person 2 : \n\n"
    f"Name : {p2.name}\n"
    f"Age : {p2.age}\n"
    f"Country : {p2.country}\n"
    f"Languages : {p2.languages}\n\n"
)
