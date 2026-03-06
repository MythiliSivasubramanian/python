"""
python/05_Lists/lists_basics_demo.py

Lists - Basics Demo:
    1. Ordered nature of lists
    2. Duplicate values support
    3. Mutability
        3.1 Adding elements: 
            - list.insert(index, value)(list len changes)
            - list.append(value) (list len changes)
            - list[index] = value (replace; list len unchanged)
        3.2 Concatenation:
            - list1 + list2 (creates new list)
            - list1.extend(list2) (in-place)
        3.3 Removing elements:
            - list.pop()
            - list.pop(index)
            - list.remove(value)
    4. Mixed data types in one list
    5. Membership check with `in`
    6. Sorting
        - list.sort() (in-place)
        - sorted(list_obj) (new list)
    7. Accessing elements
        7.1 Indexing (positive and negative)
        7.2 Slicing (start:stop:step)
    8. Iterating through a list
    9. Common utility operations
        - len, min, max, sum
        - count(value), index(value)
    10. Copying lists
        - aliasing vs shallow copy
    11. List comprehension
        - basic transformation
        - conditional comprehension
        - nested comprehension
"""
# Sample predefined list.
# This list contains duplicate values, which helps demonstrate list behavior.
my_list = [3, 2, 5, 5, 6, 1, 1, 2, 1]


# Lists are ordered.
# The same list keeps elements in the exact insertion order.
print(
        f"\nPrinting Original List :\n"
        f"Ordered : {my_list}"
     )

# Lists allow duplicate values.
# Here, 5 and 1 appear more than once.
print(f"\nLists allow duplicate values : {my_list}")


# Lists are mutable.
# We can add, remove, or replace values after the list is created.
#
# Add elements (length changes)
# list.insert(index, value) inserts at a specific position.

print(
        f"Original list is : {my_list}\n"
        f"Len of list is : {len(my_list)}"
    )

my_list.insert(1, "Red")

print(
        f"\nAdding elements to list :\n\n"
        f"Using list.insert(index,value) : (1,'Red') : \n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
    )

# Add elements using list.append(value).
# append() always adds to the end of the list.
my_list.append(100)
print(
        f"Using list.append(100) : \n\n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
     )

# Replace using list[index] = value.
# This updates an existing element, so list length does NOT change.

my_list[1] = {1: 'one', 2: 'two'}
print(
        f"Using list[1] = {{1:'one',2:'two'}} : \n\n"
        f"\tUpdated list is : {my_list}\n"
        f"\tLen of list : {len(my_list)}\n\n"
     )


# Removing elements from a list
#
# list.pop() removes and returns the last item by default.
removed_last = my_list.pop()
print(f"Removing elements :\n\n"
      f"Using list.pop() :"
      f"\tremoved {removed_last}, updated list : {my_list}\n")


# list.pop(index) removes and returns the item at the given index.
removed_index_4 = my_list.pop(4)
print(f"Using list.pop(4) : "
      f"\tremoved {removed_index_4} from index 4, updated list : {my_list}\n")


# list.remove(value) removes the first occurrence of that value.
my_list.remove(1)
print(f"Using list.remove(1) : "
      f"\tremoves element 1 of 1st occurrence : {my_list}\n\n")


# Lists accept mixed data types.
# This list now contains int and dict values together.
print(f"List accepts all data types as its elements : \n"
      f"{my_list}\n\n")


# Checking membership in a list.
# The `in` keyword returns True if value exists; otherwise False.

print(f"Checking elements in list : \n"
      f"Using Keyword 'in' returns True or False \n"
      f"Is 6 in my_list : {6 in my_list}\n"
      f"Is 99 in my_list : {99 in my_list}\n\n")


# Concatenating two lists
# Method 1: Using + creates a NEW list, originals remain unchanged.
list_a = [10, 20, 30]
list_b = [40, 50]
combined_plus = list_a + list_b

print("Concatenating lists using + :")
print(f"\tlist_a         : {list_a}")
print(f"\tlist_b         : {list_b}")
print(f"\tlist_a + list_b: {combined_plus}\n")

# Method 2: Using .extend() adds elements to the existing list in place.
list_a.extend(list_b)
print("Concatenating lists using list.extend(other_list) :")
print(f"\tAfter extend, list_a is updated in place: {list_a}")
print(f"\tlist_b remains unchanged                : {list_b}\n")


# Sorting list elements
# Note: Sorting works only when elements are comparable.
# Since `my_list` has mixed types (int + dict), use a separate numeric list.
numbers_for_sort = [9, 2, 11, 5, 2, 8]
print(f"Original numeric list for sorting: {numbers_for_sort}")

# sort() modifies the same list object (in-place).
numbers_for_sort.sort()
print(f"After numbers_for_sort.sort() (ascending): {numbers_for_sort}")

# sorted(iterable) returns a new sorted list and leaves original unchanged.
another_numbers = [4, 1, 7, 3]
sorted_copy = sorted(another_numbers, reverse=True)
print(f"\nOriginal another_numbers list             : {another_numbers}")
print(f"Result of sorted(..., reverse=True) (new): {sorted_copy}\n")


# Accessing elements of a list
letters = ["a", "b", "c", "d", "e", "f"]
print(f"Base list for indexing and slicing: {letters}\n")

# Indexing: fetch a single item by position.
print(f"Indexing examples:")
print(f"\tletters[0]  -> {letters[0]}   (first element)")
print(f"\tletters[3]  -> {letters[3]}   (element at index 3)")
print(f"\tletters[-1] -> {letters[-1]}  (last element)\n")

# Slicing: fetch a range/subset.
# Format: list[start:stop:step]
print("Slicing examples:")
print(f"\tletters[1:4]   -> {letters[1:4]}   (index 1 to 3)")
print(f"\tletters[:3]    -> {letters[:3]}    (start to index 2)")
print(f"\tletters[3:]    -> {letters[3:]}    (index 3 to end)")
print(f"\tletters[-4:-1] -> {letters[-4:-1]} (negative slicing)")
print(f"\tletters[::2]   -> {letters[::2]}   (every 2nd element)")
print(f"\tletters[::-1]  -> {letters[::-1]}  (reversed list)\n")


# Iterating through a list
# Use a for loop when you need to process each element one by one.
fruits = ["apple", "banana", "cherry"]
print("Iteration examples:")
for fruit in fruits:
    print(f"\tFruit item -> {fruit}")
print()


# Common utility operations on numeric lists
scores = [88, 92, 75, 92, 100]
print(f"Utility operations on scores list: {scores}")
print(f"\tlen(scores)          -> {len(scores)}")
print(f"\tmin(scores)          -> {min(scores)}")
print(f"\tmax(scores)          -> {max(scores)}")
print(f"\tsum(scores)          -> {sum(scores)}")
print(f"\tscores.count(92)     -> {scores.count(92)}")
print(f"\tscores.index(75)     -> {scores.index(75)}\n")


# Copying lists: aliasing vs shallow copy
# `alias = original` points to same object; change in one affects the other.
# `copy()` creates a new top-level list object.
original = [1, 2, 3]
alias = original
shallow_copy = original.copy()

alias.append(4)
print("List copying behavior:")
print(f"\toriginal after alias.append(4): {original}")
print(f"\talias                         : {alias}")
print(f"\tshallow_copy (unchanged)      : {shallow_copy}\n")


# List comprehension
# A concise way to build lists from iterables.
base_numbers = [1, 2, 3, 4, 5, 6]

# Basic transformation: square of each number.
squares = [num * num for num in base_numbers]

# Conditional comprehension: keep only even numbers.
evens = [num for num in base_numbers if num % 2 == 0]

# Nested comprehension: flatten a matrix.
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]

print("List comprehension examples:")
print(f"\tBase numbers                 : {base_numbers}")
print(f"\tSquares                      : {squares}")
print(f"\tEven numbers                 : {evens}")
print(f"\tMatrix                       : {matrix}")
print(f"\tFlattened matrix (nested)    : {flattened}\n")
