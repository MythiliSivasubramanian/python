"""
Classes:
    1. Creating Class
    2. Creating Objects (multiple Objects)
    3. Deleting Objects
"""

# 1) Creating a class

"""
 A class is a blueprint. Objects created from this class
 will get the attributes and behavior defined here.
"""
class Sample:
    # x is a class attribute.
    # It is shared by all objects unless overridden.
    x = 5


# 2) Creating objects (multiple objects) p1 and p2
# Creating two separate objects from the same class.
p1 = Sample()
p2 = Sample()

# Printing value of x from both objects.
# Both objects read the same class attribute value.
print(f"\n\nPrinting the value of x : {p1.x}")
print(f"\nPrinting the value of x : {p2.x}")



# 3) Deleting objects

"""
We can delete an object reference using `del`.
After deletion, trying to access that variable name
raises NameError because the name no longer exists.
"""
print("\n\nDeleting object p1 : ")
del p1

try:
    print("\n",p1.x)  # This line will fail because p1 is deleted.
except NameError as error:
    print(f"\nCannot access p1 after deletion: {error}")

# p2 still exists and can be used normally.
print(f"\np2 still exists. Value of x from p2 : {p2.x}\n\n")