# Custom Exceptions

"""
Validate user input using custom exceptions.

Ask user to enter a number between 0 and 100 inclusive.
Raise custom exceptions for :
    1.negative numbers,
    2.numbers greater than 100,
    3.handles invalid non-integer input.
    
"""

class TooLargeNumberError (Exception):
    pass

class NegativeNumberError(Exception):
    pass

try:
    # Get input from User
    num = int(input("\n\nEnter a number between 0 to 100 (inclusive): "))
    
    # Negative not allowed
    if num < 0:
        raise NegativeNumberError("Negative not allowed")
    
    # Number shouldn't be grater than 100 
    if num > 100:
        raise TooLargeNumberError("Number shouldn't be grater than 100")

# Negative not allowed
except NegativeNumberError as e:
    print("Something Wrong : ", e)

# Number greater than 100
except TooLargeNumberError as e:
    print("Error : ", e)
    
# Invalid Input(symbols, Characters etc)
except ValueError as e:
    print("Invalid Input : ", e)
   
   
else:
    print(f"Success! {num} is a valid input.")
