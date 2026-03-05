"""
Python Classes:
    1. __init__ constructor
    2. Without using __init__()
    3. Setting initial values in __init__

__init__ runs automatically when an object is created and is commonly used
to initialize instance attributes.
"""

class Person:
    # Represents a person with basic profile details.

    def __init__(self, name, age, country, languages):
        # Using __init__() makes it easier to create objects with initial values.
        self.name = name
        self.age = age
        self.country = country
        self.languages = languages
    
# Create objects p1 and p2 for class Person
p1 = Person("Anderson", 22, "Norway", ["English", "Spanish", "Chinese"])
p2 = Person("Ava", 25, "Canada", ["English", "French"])

print(
    f"\n\nDetails of Person 1 : \n"
    f"Name : {p1.name}\n"
    f"Age : {p1.age}\n"
    f"Country : {p1.country}\n"
    f"Languages : {p1.languages}\n\n"
)

print(
    f"Details of Person 2 : \n"
    f"Name : {p2.name}\n"
    f"Age : {p2.age}\n"
    f"Country : {p2.country}\n"
    f"Languages : {p2.languages}\n\n"
)



"""
Without using __init__ constructor:
Without the __init__() method, we would need to set properties manually for each object
"""

class Persons:
    pass

# Create Object p_1 of class Persons
p_1 = Persons()
p_1.name = "Alex"
p_1.age = 25
p_1.country = "America"
p_1.languages = ["English", "French", "Chinese"]

# Printing the details

print("\n\nWithout using __init__ constructor : \n\n")
print(
        f"Details of the person : \n"
        f"Name : {p_1.name}\n"
        f"Age : {p_1.age}\n"
        f"Country : {p_1.country}\n"
        f"Languages : {p_1.languages}\n\n"
    )


# Setting initial values when using __init__ method():
class PersonsSample:
    def __init__(self, name, country, age=20, language=None):
        # Avoid mutable default arguments like [] in function signatures.
        if language is None:
            language = ["Mexican", "English"]

        self.name = name
        self.country = country
        self.age = age
        self.language = language

person_1 = PersonsSample("Anna", "Mexico")
person_2 = PersonsSample("Hella", "London", 33, ["French"])

print(
      f"Setting initial values when using __init__ method() : \n\n"
      f"Details of Person 1 : \n"
      f"Name : {person_1.name}\n"
      f"Age : {person_1.age}\n"
      f"Country : {person_1.country}\n"
      f"Languages : {person_1.language}\n\n"
)

print(
      f"Details of person 2 : \n\n"
      f"Name : {person_2.name}\n"
      f"Age : {person_2.age}\n"
      f"Country : {person_2.country}\n"
      f"Languages : {person_2.language}\n\n"
)