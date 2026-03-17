# Get input from user and divide by 10
"""
It keeps asking the user until valid input is given
Only exits when division is successful
"""
count = 0
success = False
while count < 3:
    try:
        # Convert input from string to int
        num = int(input("Enter a number : "))
        print(10 / num)
      
    except ZeroDivisionError as e:
        print("Opps! The Error is  : ", e)
        count += 1
    except ValueError as e:
        print("Invalid Input : ", e)
        count += 1
    else:
        print("Success!")
        success = True
        break
if not success:
    print("Try again after some time. Too many attempts")
    
print("\nExecution Completed!")

