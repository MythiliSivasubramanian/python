"""
python/08_Strings/strings_basics_demo.py

Strings - Basics Demo:
    1. Immutability of strings
    2. String concatenation
    3. String repetition
    4. Accessing characters (indexing and slicing)
    5. String methods
        5.1 Case conversion: upper(), lower(), title(), capitalize()
        5.2 Whitespace handling: strip(), lstrip(), rstrip()
        5.3 Searching: find(), index(), rfind(), rindex()
        5.4 Replacing: replace()
        5.5 Splitting: split(), rsplit(), splitlines()
        5.6 Joining: join()
        5.7 Checking: isalpha(), isdigit(), isalnum(), isspace(), startswith(), endswith()
    6. String formatting
        6.1 % formatting
        6.2 str.format()
        6.3 f-strings
    7. Membership check with `in`
    8. Iterating through a string
    9. Common utility operations
        - len(), min(), max()
        - count(substring), index(substring)
    10. String comparison
    11. Escape sequences
    12. Raw strings
    13. Multiline strings
"""

# Sample predefined string.
sample_string = "Hello, World! Welcome to Python programming."

print(f"Sample string: {sample_string}\n")

# Strings are immutable.
# Once created, individual characters cannot be changed.
# Attempting to modify will raise an error.
print("Strings are immutable:")
try:
    # This will fail
    sample_string[0] = 'h'
except TypeError as e:
    print(f"Error when trying to modify: {e}")
print(f"Original string remains unchanged: {sample_string}\n")

# String concatenation
# Method 1: Using + operator
str1 = "Hello"
str2 = "World"
concatenated = str1 + ", " + str2 + "!"
print(f"String concatenation using +:")
print(f"\tstr1: {str1}")
print(f"\tstr2: {str2}")
print(f"\tstr1 + ', ' + str2 + '!': {concatenated}\n")

# Method 2: Using join() for multiple strings
words = ["Hello", "World", "from", "Python"]
joined = " ".join(words)
print(f"String joining using join():")
print(f"\twords: {words}")
print(f"\t' '.join(words): {joined}\n")

# String repetition
repeated = "Ha" * 3
print(f"String repetition using *:")
print(f"\t'Ha' * 3: {repeated}\n")

# Accessing characters: Indexing
print("String indexing:")
print(f"\tsample_string[0]: {sample_string[0]}  (first character)")
print(f"\tsample_string[7]: {sample_string[7]}  (8th character)")
print(f"\tsample_string[-1]: {sample_string[-1]} (last character)\n")

# Accessing characters: Slicing
print("String slicing:")
print(f"\tsample_string[0:5]: {sample_string[0:5]}   (first 5 characters)")
print(f"\tsample_string[7:12]: {sample_string[7:12]} (characters 8-12)")
print(f"\tsample_string[::-1]: {sample_string[::-1]} (reversed string)")
print(f"\tsample_string[::2]: {sample_string[::2]}   (every 2nd character)\n")

# String methods - Case conversion
test_string = "hello world"
print("String case conversion methods:")
print(f"\tOriginal: {test_string}")
print(f"\tupper(): {test_string.upper()}")
print(f"\tlower(): {test_string.lower()}")
print(f"\ttitle(): {test_string.title()}")
print(f"\tcapitalize(): {test_string.capitalize()}\n")

# String methods - Whitespace handling
whitespace_string = "  hello world  "
print("String whitespace handling:")
print(f"\tOriginal: '{whitespace_string}'")
print(f"\tstrip(): '{whitespace_string.strip()}'")
print(f"\tlstrip(): '{whitespace_string.lstrip()}'")
print(f"\trstrip(): '{whitespace_string.rstrip()}'\n")

# String methods - Searching
search_string = "Hello, World! Hello again."
print("String searching methods:")
print(f"\tString: {search_string}")
print(f"\tfind('World'): {search_string.find('World')}")
print(f"\tfind('Python'): {search_string.find('Python')}  (-1 if not found)")
print(f"\trfind('Hello'): {search_string.rfind('Hello')}")
print(f"\tindex('World'): {search_string.index('World')}")
print(f"\trindex('Hello'): {search_string.rindex('Hello')}\n")

# String methods - Replacing
replace_string = "I like cats. Cats are cute."
print("String replacing:")
print(f"\tOriginal: {replace_string}")
print(f"\treplace('cats', 'dogs'): {replace_string.replace('cats', 'dogs')}\n")

# String methods - Splitting
split_string = "apple,banana,cherry,date"
print("String splitting:")
print(f"\tOriginal: {split_string}")
print(f"\tsplit(','): {split_string.split(',')}")
print(f"\tsplit(',', 2): {split_string.split(',', 2)}  (max 2 splits)\n")

# Multiline string splitting
multiline = "Line 1\nLine 2\nLine 3"
print("Multiline string splitting:")
print(f"\tOriginal: {repr(multiline)}")
print(f"\tsplitlines(): {multiline.splitlines()}\n")

# String methods - Checking
check_string = "Python123"
print("String checking methods:")
print(f"\tString: {check_string}")
print(f"\tisalpha(): {check_string.isalpha()}")
print(f"\tisdigit(): {check_string.isdigit()}")
print(f"\tisalnum(): {check_string.isalnum()}")
print(f"\tisspace(): {'   '.isspace()}")
print(f"\tstartswith('Py'): {check_string.startswith('Py')}")
print(f"\tendswith('23'): {check_string.endswith('23')}\n")

# String formatting
name = "Alice"
age = 30

# % formatting
formatted_percent = "My name is %s and I am %d years old." % (name, age)
print("String formatting - % operator:")
print(f"\t\"My name is %s and I am %d years old.\" % (name, age)")
print(f"\tResult: {formatted_percent}\n")

# str.format()
formatted_format = "My name is {} and I am {} years old.".format(name, age)
print("String formatting - str.format():")
print(f"\t\"My name is {{}} and I am {{}} years old.\".format(name, age)")
print(f"\tResult: {formatted_format}\n")

# f-strings
formatted_f = f"My name is {name} and I am {age} years old."
print("String formatting - f-strings:")
print(f"\tf\"My name is {{name}} and I am {{age}} years old.\"")
print(f"\tResult: {formatted_f}\n")

# Membership check
print("Membership check with 'in':")
print(f"\t'World' in sample_string: {'World' in sample_string}")
print(f"\t'Python' in sample_string: {'Python' in sample_string}\n")

# Iterating through a string
print("Iterating through a string:")
for char in "Hello":
    print(f"\tCharacter: {char}")
print()

# Common utility operations
utility_string = "hello world hello"
print(f"Utility operations on string: '{utility_string}'")
print(f"\tlen(): {len(utility_string)}")
print(f"\tmin(): '{min(utility_string)}'  (lowest ASCII character)")
print(f"\tmax(): '{max(utility_string)}'  (highest ASCII character)")
print(f"\tcount('l'): {utility_string.count('l')}")
print(f"\tcount('hello'): {utility_string.count('hello')}")
print(f"\tindex('world'): {utility_string.index('world')}\n")

# String comparison
print("String comparison:")
print(f"\t'abc' < 'abd': {'abc' < 'abd'}  (lexicographical order)")
print(f"\t'ABC' < 'abc': {'ABC' < 'abc'}  (ASCII values)")
print(f"\t'hello' == 'hello': {'hello' == 'hello'}")
print(f"\t'hello' == 'Hello': {'hello' == 'Hello'}\n")

# Escape sequences
print("Escape sequences:")
print("\t\\n - Newline")
print("\t\\t - Tab")
print("\t\\\\ - Backslash")
print("\t\\\" - Double quote")
print("\t\\\' - Single quote")
print(f"Example: 'Hello\\nWorld' -> {repr('Hello\nWorld')}\n")

# Raw strings
print("Raw strings:")
print(f"\tr'Hello\\nWorld' -> {repr(r'Hello\nWorld')}")
print(f"\tRegular: 'C:\\\\Users\\\\file.txt' -> {'C:\\Users\\file.txt'}")
print(f"\tRaw: r'C:\\\\Users\\\\file.txt' -> {r'C:\Users\file.txt'}\n")

# Multiline strings
multiline_string = """This is a
multiline string
that spans multiple lines."""
print("Multiline strings:")
print(f"\t{repr(multiline_string)}")
print(f"\tActual output:")
print(multiline_string)