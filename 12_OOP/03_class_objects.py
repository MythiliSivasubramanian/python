# Python Objects & Classes Micro-Exploration


# Create a class Dog
class Dog:
    pass

# Create 2 objects a and c
a = Dog()
b = a
c = Dog()

print("\n\nObjects of class Dog and type of each objects : ")
print(f"\tObject a : {a}\t\tType: {type(a)}")
print(f"\tObject b : {b}\t\tType: {type(b)}")
print(f"\tObject c : {c}\t\tType: {type(c)}\n")


print(f"Is type(a) equal to type(b)? \t{type(a) == type(b)}")
print(f"Do a and b refer to the same object? \t{a is b}")
print(f"Do b and c refer to the same object? \t{b is c}")
print(f"Do a and c refer to the same object? \t{a is c}\n")
print(f"IDs of objects: \n"
      f"a = {id(a)}\n"
      f"b = {id(b)}\n"
      f"c = {id(c)}\n\n")


print(f"Type of class Dog : {type(Dog)}")
print("-" * 40)
print(f"Type of int: {type(int)}")
print(f"Type of str: {type(str)}")
print(f"Type of list: {type(list)}")
print("-" * 40)

# Sample class experiments

class Sample:
    pass

# Creating objects
x = Sample()
y = x
z = y

print("\n Sample class objects : ")
print(f"\tObject x : {x}\tID: {id(x)}")
print(f"\tObject y : {y}\tID: {id(y)}")
print(f"\tObject z : {z}\tID: {id(z)}\n")

print(f"Do x and y refer to the same object? {x is y}")
print(f"Do y and z refer to the same object? {y is z}")
print(f"Do x and z refer to the same object? {x is z}\n\n")