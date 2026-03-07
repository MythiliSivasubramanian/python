"""
python/06_Dictionaries/dictionaries_basics_demo.py

Dictionaries - Basics Demo:
    1. Ordered mapping (insertion order is preserved)
    2. Keys are unique (duplicate key updates value)
    3. Mutable object (add/update/remove key-value pairs)
    4. Creating dictionaries
        - Using {}
        - Using dict()
        - Converting other datatypes to dict using dict()
    5. Accessing values
        - dict[key]
        - dict.get(key, default)
    6. Adding and updating items
        - dict[new_key] = value
        - dict.update({...})
        - dict.setdefault(key, default)
    7. Removing items
        - pop(key[, default])
        - popitem()
        - del dict[key]
        - clear()
    8. Membership checks
        - key in dict
    9. Common dictionary views
        - keys(), values(), items()
    10. Iteration patterns
        - Looping over keys, values, and key-value pairs
    11. Copying dictionaries
        - aliasing vs shallow copy
    12. Nested dictionary access
    13. Dictionary comprehension
        - basic
        - conditional
    14. defaultdict (from collections)
        - automatic default value for missing keys
        - useful for counting and grouping
    15. Hashing and hashable keys
        - keys must be immutable/hashable
        - unhashable keys raise TypeError
"""
from collections import defaultdict

# 1) Ordered mapping
student = {
    "name": "Anita",
    "age": 21,
    "course": "Data Science"
}
print("\nOriginal dictionary (ordered by insertion):")
print(student)


# 2) Keys are unique
# If the same key is repeated, latest value overwrites earlier one.
duplicate_key_demo = {"id": 101, "id": 202}
print("\nDuplicate key behavior:")
print(f"Only last value is kept for key 'id': {duplicate_key_demo}")


# 3 & 4) Mutable + creating dictionaries
# Method 1: Literal syntax {}
employee = {"emp_id": "E101", "name": "John"}

# Method 2: dict() constructor
employee_2 = dict(emp_id="E102", name="Sara")

# dict() can also convert compatible datatypes into dictionary.
# Each item must be a (key, value) pair.
pairs = [("city", "Munich"), ("country", "Germany")]
converted_dict = dict(pairs)

print("\nDictionary creation methods:")
print(f"employee using {{}}   : {employee}")
print(f"employee_2 using dict(): {employee_2}")
print(f"dict(list_of_pairs)   : {converted_dict}")



# 5) Accessing values
# Access with [] raises KeyError for missing key.
print("\nAccessing values:")
print(f"employee['name'] -> {employee['name']}")

# Access with get() is safe for missing keys.
print(f"employee.get('salary') -> {employee.get('salary')}")
print(f"employee.get('salary', 'Not Available') -> {employee.get('salary', 'Not Available')}")


# 6) Adding and updating items
# Add a new key-value pair.
employee["department"] = "AI"

# Update multiple keys at once.
employee.update({"city": "Berlin", "name": "John K"})

# setdefault adds key only if missing.
employee.setdefault("experience", "Beginner")

# This call does nothing because key already exists.
employee.setdefault("name", "Will Not Replace")

print("\nAfter add/update/setdefault:")
print(employee)


# 7) Removing items
# pop(key, default): removes key and returns its value.
removed_dept = employee.pop("department", None)

# popitem(): removes and returns last inserted key-value pair.
removed_last_item = employee.popitem()

# del dict[key]: removes specific key.
del employee["city"]

print("\nAfter removals (pop, popitem, del):")
print(f"removed_dept      -> {removed_dept}")
print(f"removed_last_item -> {removed_last_item}")
print(f"employee now      -> {employee}")

# clear(): remove all entries.
temp = {"a": 1, "b": 2}
temp.clear()
print(f"After clear(), temp -> {temp}")



# 8) Membership checks
# `in` checks keys, not values.
print("\nMembership checks:")
print(f"'name' in employee  -> {'name' in employee}")
print(f"'John K' in employee -> {'John K' in employee}")


# 9) Dictionary views: keys, values, items
print("\nDictionary views:")
print(f"Keys   -> {list(student.keys())}")
print(f"Values -> {list(student.values())}")
print(f"Items  -> {list(student.items())}")

# 10) Iteration patterns
print("\nIteration examples:")

print("Looping over keys:")
for key in student:
    print(f"  {key}")

print("Looping over values:")
for value in student.values():
    print(f"  {value}")

print("Looping over key-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")


# 11) Copying dictionaries: aliasing vs shallow copy
original = {"x": 1, "y": 2}
alias = original                # Same object reference
shallow_copy = original.copy()  # New dictionary object

alias["z"] = 3

print("\nCopying behavior:")
print(f"original     -> {original}")
print(f"alias        -> {alias}")
print(f"shallow_copy -> {shallow_copy}")


# 12) Nested dictionary access
classroom = {
    "student_1": {"name": "Asha", "marks": 91},
    "student_2": {"name": "Rahul", "marks": 84}
}

print("\nNested dictionary access:")
print(f"student_1 name  -> {classroom['student_1']['name']}")
print(f"student_2 marks -> {classroom['student_2']['marks']}")


# 13) Dictionary comprehension
# Basic comprehension: map number to square.
squares = {n: n * n for n in range(1, 6)}

# Conditional comprehension: keep only even squares.
even_squares = {n: n * n for n in range(1, 11) if n % 2 == 0}

print("\nDictionary comprehension examples:")
print(f"squares      -> {squares}")
print(f"even_squares -> {even_squares}\n")


# 14) defaultdict
# defaultdict automatically creates a default value for missing keys.
# This avoids manual checks like: if key not in dict: dict[key] = 0

# Counting example with int as default factory (default value = 0)
letters = "mississippi"
char_count = defaultdict(int)

for ch in letters:
    char_count[ch] += 1

print("defaultdict counting example:")
print(f"Input string -> {letters}")
print(f"Counts       -> {dict(char_count)}")

# Grouping example with list as default factory (default value = [])
words = ["apple", "ant", "ball", "bat", "cat"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print("\ndefaultdict grouping example:")
print(f"Words        -> {words}")
print(f"Grouped      -> {dict(grouped)}\n")


# 15) Hashing and hashable keys
# Dictionary lookup is based on hashing.
# A key must be hashable (its hash value must not change during its lifetime).
# Common hashable types: int, float, str, tuple (only if all elements are hashable).
# Common unhashable types: list, dict, set.

print("Hashing basics:")
print(f"hash(42)        -> {hash(42)}")
print(f"hash('python')  -> {hash('python')}")
print(f"hash((1, 2, 3)) -> {hash((1, 2, 3))}")

# Valid hashable keys
hash_key_demo = {
    1: "int key",
    "id": "string key",
    (10, 20): "tuple key"
}
print(f"\nDictionary with hashable keys -> {hash_key_demo}")

# Unhashable key example (handled safely)
try:
    invalid_key_dict = {[1, 2, 3]: "list key not allowed"}
    print(invalid_key_dict)
except TypeError as exc:
    print(f"Using list as dict key raises -> {exc}\n")
