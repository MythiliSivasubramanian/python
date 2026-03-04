"""
python/05_Lists/list_basics_demo.py

Lists:
    1. Ordered
    2. Allows Duplicates
    3. Mutable 
        3.1 Add elements:
            Len of list is changed vs len of the list unchanged
            list.insert(i,v) alters len of the list, list.append(v) adds to end of the list
            list[i] = v replaces the value at index hence len unchanged
            
        3.2 Removing elements of list
            List.pop(), list.pop(index)
            list.remove(value)
    4. Accepts all data types as its elements
    5. Checking elements in list
        keyword 'in' returns True or False
        

"""
# Sample predefined list
my_list = [3,2,5,5,6,1,1,2,1]


# Lists are ordered       
print(
        f"\nPrinting Original List :\n"
        f"Ordered : {my_list}"
     )

# Lists allow duplicate values
print(f"\nLists allow duplicate values : {my_list}")


# Lists are mutable 
# Add elements (len of list is altered)
# list.insert(i,v) alters len of the list

print(
        f"Original list is : {my_list}\n"
        f"Len of list is : {len(my_list)}"
    )

my_list.insert(1,"Red")

print(
        f"\nAdding elements to list :\n\n"
        f"Using list.insert(index,value) : (1,'Red') : \n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
    )

# Add elements using list.append 
# Adds to the end of list
my_list.append(100) 
print(
        f"Using list.append(100) : \n\n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
     )

# Add using list[i] = v
# replaces the value at the specified index, doesnt alter the len of index

my_list[1] = {1:'one',2:'two'}
print(
        f"Using list[1] = {{1:'one',2:'two'}} : \n\n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
     )


# Removing elements
# Using list.pop() to remove last added element

my_list.pop()
print(f"Removing elements :\n\n"
      f"Using list.pop() :"
      f"\tremoves last item : {my_list}\n")


# using list.pop(i)
# removes the element at specified index
my_list.pop(4)
print(f"Using list.pop(4) : " 
      f"\tremoves element at 4th index : {my_list}\n")


# using list.remove(value)
# removes the specified value of 1st occurrence
my_list.remove(1)
print(f"Using list.remove(1) : "
      f"\tremoves element 1 of 1st occurrence : {my_list}\n\n")



# Accepts all data types as its elements
print(f"List accepts all data types as its elements : \n"
      f"{my_list}\n\n")


# Checking elements in list
# Keyword in returns True or False

print(f"Checking elements in list : \n"
      f"Using Keyword 'in' returns True or False \n"
      f"Is 6 in my_list : {6 in my_list}\n\n")
