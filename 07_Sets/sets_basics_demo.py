"""
python/07_Sets/sets_basics_demo.py

Sets - Basics Demo:
    1. Unordered collection of unique elements
    2. Duplicate values are removed automatically
    3. Mutable set object (add/update/remove)
    4. Creating sets
        - Using {}
        - Using set(iterable)
        - Empty set with set() (not {})
    5. Membership check with `in`
    6. Adding and updating
        - add()
        - update()
    7. Removing items
        - remove()
        - discard()
        - pop()
        - clear()
    8. Set operations
        - union
        - intersection
        - difference
        - symmetric difference
        - intersection_update()
        - difference_update()
        - symmetric_difference_update()
    9. Relationship checks
        - issubset(), issuperset(), isdisjoint()
    10. Iterating through a set
    11. Copying sets
        - aliasing vs copy()
    12. Set comprehension
        - basic
        - conditional
    13. Hashing and set elements
        - set elements must be hashable
    14. frozenset (immutable set)
"""

# 1) Unordered + unique behavior
numbers = {1, 2, 3, 2, 1, 4, 5}
print("\nSet with duplicates in input:")
print(f"numbers -> {numbers}")
print("Duplicates are removed automatically in a set.")


# 2, 3, 4) Creating sets and mutability
# Method 1: Using set literal {}
fruits = {"apple", "banana", "cherry"}

# Method 2: set(iterable) converts iterable to set
letters_from_word = set("hello")

# Important: {} creates an empty dict, not an empty set.
empty_set = set()

print("\nSet creation examples:")
print(f"fruits             -> {fruits}")
print(f"set('hello')       -> {letters_from_word}")
print(f"empty_set via set() -> {empty_set}")


# 5) Membership check
print("\nMembership checks:")
print(f"'apple' in fruits  -> {'apple' in fruits}")
print(f"'orange' in fruits -> {'orange' in fruits}")


# 6) Adding and updating
# add() inserts one element.
fruits.add("orange")

# update() inserts multiple elements from iterable.
fruits.update(["grape", "mango", "apple"])  # 'apple' already exists

print("\nAfter add() and update():")
print(f"fruits -> {fruits}")


# 7) Removing items
# remove(x) raises KeyError if x not found.
fruits.remove("banana")

# discard(x) does NOT raise error if x not found.
fruits.discard("pear")

# pop() removes and returns an arbitrary element (because sets are unordered).
popped_item = fruits.pop()

print("\nAfter remove(), discard(), pop():")
print(f"popped_item -> {popped_item}")
print(f"fruits      -> {fruits}")

# clear() removes all elements.
temp_set = {10, 20, 30}
temp_set.clear()
print(f"temp_set after clear() -> {temp_set}")


# 8) Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nSet operations:")
print(f"a                -> {a}")
print(f"b                -> {b}")
print(f"a union b        -> {a | b}")
print(f"a intersection b -> {a & b}")
print(f"a difference b   -> {a - b}")
print(f"a symmetric diff -> {a ^ b}")

# Methods can take any iterable (Python converts internally to set behavior).
list_input = [4, 5, 6, 7]
print(f"a.union([4, 5, 6, 7])        -> {a.union(list_input)}")
print(f"a.intersection([4, 5, 6, 7]) -> {a.intersection(list_input)}")

# Binary operators require both operands to already be sets.
try:
    operator_demo = a | list_input
    print(operator_demo)
except TypeError as exc:
    print(f"a | [4, 5, 6, 7] raises -> {exc}")

# intersection_update() keeps only common elements by modifying the set in place.
a_inplace = {1, 2, 3, 4}
a_inplace.intersection_update(b)
print(f"a after intersection_update(b) -> {a_inplace}")

# difference_update() removes elements found in the other set (in-place).
d_inplace = {1, 2, 3, 4}
d_inplace.difference_update(b)
print(f"d after difference_update(b)   -> {d_inplace}")

# symmetric_difference_update() keeps elements in either set, but not both (in-place).
s_inplace = {1, 2, 3, 4}
s_inplace.symmetric_difference_update(b)
print(f"s after symmetric_difference_update(b) -> {s_inplace}")


# 9) Relationship checks
x = {1, 2}
y = {1, 2, 3, 4}
z = {7, 8}

print("\nRelationship checks:")
print(f"x.issubset(y)   -> {x.issubset(y)}")
print(f"y.issuperset(x) -> {y.issuperset(x)}")
print(f"x.isdisjoint(z) -> {x.isdisjoint(z)}")


# 10) Iterating through a set
colors = {"red", "green", "blue"}
print("\nIteration example:")
for color in colors:
    print(f"  color -> {color}")


# 11) Copying sets: aliasing vs copy
original = {1, 2, 3}
alias = original         # Same object
copied = original.copy() # New object

alias.add(4)

print("\nCopying behavior:")
print(f"original -> {original}")
print(f"alias    -> {alias}")
print(f"copied   -> {copied}")


# 12) Set comprehension
# Basic: squares of numbers
squares = {n * n for n in range(1, 6)}

# Conditional: even numbers only
evens = {n for n in range(1, 11) if n % 2 == 0}

print("\nSet comprehension examples:")
print(f"squares -> {squares}")
print(f"evens   -> {evens}")


# 13) Hashing and set elements
# Set elements must be hashable/immutable-like objects.
# int, str, tuple (with hashable elements) are valid.
valid_set = {1, "python", (10, 20)}
print("\nHashable elements in set:")
print(f"valid_set -> {valid_set}")

# list is unhashable, so adding it to set raises TypeError.
try:
    invalid_set = {1, 2, [3, 4]}
    print(invalid_set)
except TypeError as exc:
    print(f"Using list inside set raises -> {exc}")


# 14) frozenset (immutable set)
# frozenset cannot be modified after creation.
immutable_group = frozenset([1, 2, 3, 2])
print("\nfrozenset example:")
print(f"immutable_group -> {immutable_group}")

# Uncommenting next line would raise AttributeError:
# immutable_group.add(4)
