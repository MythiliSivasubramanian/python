git """
python/08_Strings/strings_advanced_demo.py

Strings - Advanced Concepts Demo:
    1. Regular expressions with strings
        1.1 Basic pattern matching
        1.2 Finding all matches
        1.3 Replacing with regex
        1.4 Splitting with regex
    2. Unicode and encoding
        2.1 Unicode strings
        2.2 Encoding and decoding
        2.3 Handling special characters
    3. String templates
    4. Advanced string formatting
        4.1 Format specifications
        4.2 Alignment and padding
        4.3 Number formatting
    5. String interning
    6. Performance considerations
        6.1 String concatenation vs join
        6.2 String building with lists
    7. Text processing utilities
        7.1 Tokenization
        7.2 Case folding
        7.3 Translating characters
    8. Common string algorithms
        8.1 Checking palindromes
        8.2 Finding anagrams
        8.3 String compression (simple)
"""

import re
from string import Template

# Regular expressions with strings
print("=== Regular Expressions ===")

sample_text = "The email addresses are user1@example.com and user2@test.org. Visit https://www.example.com for more info."

# Basic pattern matching
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, sample_text)
print(f"Emails found: {emails}")

# Finding all matches with groups
url_pattern = r'https?://(www\.)?([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})'
urls = re.findall(url_pattern, sample_text)
print(f"URLs found: {urls}")

# Replacing with regex
censored = re.sub(email_pattern, '[EMAIL]', sample_text)
print(f"Censored text: {censored}")

# Splitting with regex
words = re.split(r'\s+', "This   is    a    test")
print(f"Split by whitespace: {words}\n")

# Unicode and encoding
print("=== Unicode and Encoding ===")

# Unicode strings
unicode_string = "Hello, 世界! 🌍"
print(f"Unicode string: {unicode_string}")
print(f"Length: {len(unicode_string)}")

# Encoding and decoding
utf8_bytes = unicode_string.encode('utf-8')
print(f"UTF-8 encoded: {utf8_bytes}")
decoded = utf8_bytes.decode('utf-8')
print(f"Decoded back: {decoded}")

# Handling special characters
special_chars = "café, naïve, résumé"
print(f"Special characters: {special_chars}")
normalized = special_chars.casefold()
print(f"Case folded: {normalized}\n")

# String templates
print("=== String Templates ===")

template = Template("Hello, $name! Welcome to $place.")
result = template.substitute(name="Alice", place="Wonderland")
print(f"Template result: {result}")

# Safe substitution
safe_template = Template("Hello, $name! Welcome to $place.")
safe_result = safe_template.safe_substitute(name="Bob")  # place is missing
print(f"Safe substitution: {safe_result}\n")

# Advanced string formatting
print("=== Advanced String Formatting ===")

# Format specifications
pi = 3.14159265359
print(f"Default: {pi}")
print(f"Fixed: {pi:.2f}")
print(f"Scientific: {pi:.2e}")
print(f"Percentage: {0.75:.1%}")

# Alignment and padding
names = ["Alice", "Bob", "Catherine"]
for name in names:
    print(f"|{name:<10}|{name:^10}|{name:>10}|")

# Number formatting
number = 1234567.89
print(f"With commas: {number:,.2f}")
print(f"Binary: {42:b}")
print(f"Hex: {255:x}")
print(f"Octal: {64:o}\n")

# String interning
print("=== String Interning ===")

# Python automatically interns small strings and identifiers
str1 = "hello"
str2 = "hello"
print(f"str1 is str2: {str1 is str2}")  # True due to interning

# Manual interning
interned = sys.intern("world")
interned2 = sys.intern("world")
print(f"Interned strings are same object: {interned is interned2}\n")

# Performance considerations
print("=== Performance Considerations ===")

import time

# Inefficient: repeated concatenation
start = time.time()
result = ""
for i in range(10000):
    result += str(i)
inefficient_time = time.time() - start
print(f"Inefficient concatenation time: {inefficient_time:.4f}s")

# Efficient: using join
start = time.time()
parts = [str(i) for i in range(10000)]
result = "".join(parts)
efficient_time = time.time() - start
print(f"Efficient join time: {efficient_time:.4f}s")
print(f"Join is {inefficient_time/efficient_time:.1f}x faster\n")

# Text processing utilities
print("=== Text Processing Utilities ===")

text = "This is a SAMPLE text with Mixed CASE."

# Tokenization (simple split)
tokens = text.split()
print(f"Tokens: {tokens}")

# Case folding (better than lower() for case-insensitive comparison)
folded = text.casefold()
print(f"Case folded: {folded}")

# Translating characters
translator = str.maketrans("aeiou", "12345")
translated = text.translate(translator)
print(f"Translated vowels: {translated}")

# Removing punctuation
import string
no_punct = text.translate(str.maketrans("", "", string.punctuation))
print(f"No punctuation: {no_punct}\n")

# Common string algorithms
print("=== Common String Algorithms ===")

# Checking palindromes
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_words = ["radar", "A man a plan a canal Panama", "hello"]
for word in test_words:
    print(f"'{word}' is palindrome: {is_palindrome(word)}")

# Finding anagrams
def are_anagrams(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

print(f"'listen' and 'silent' are anagrams: {are_anagrams('listen', 'silent')}")

# Simple string compression (run-length encoding)
def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    result = "".join(compressed)
    return result if len(result) < len(s) else s

test_string = "aaabbbcccaaa"
compressed = compress_string(test_string)
print(f"Original: '{test_string}', Compressed: '{compressed}'")