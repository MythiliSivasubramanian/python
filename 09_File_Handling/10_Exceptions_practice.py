"""
1. Get a number from user
2. Handle:
        Raise error if negative
        invalid input (abc)
        division by zero (0)
3. If valid number, divide as 10 / input
4. Program must NOT crash

"""

try:    
    # Get Input from user
    num = int(input("\n\nEnter a number : "))
    result = 10 / num
    
    # Raise error if negative
    if num < 0:
        raise ValueError("Negative numbers not allowed")
   
# Invalid input (symbols, characters etc)
except ValueError:
    print("\nInvalid Number!. Please enter a valid number")
    
# Input as 0
except ZeroDivisionError as e:
    print("\nCannot divide by zero!")
    
# If no error in Try block execute else block
else:
    
    print("\nSuccess!. Result is ",result)

finally:
    print("\nThank you!")
    


try:
    data = [10, 20, 30]
    print(data[10])
    
# Index out of range
except IndexError as e:
    print("\nError Occurred : ",e)

    
    
"""
Write a program that:
    1. takes a number from user
    2. if number is greater than 100, raise an error: "Number too large"
"""

try:
    # Get input from User
    input_1 = int(input("\nEnter a number : "))
    
    if input_1 > 100:
        raise ValueError("Number too large")
    
except ValueError as e:
    print(e)