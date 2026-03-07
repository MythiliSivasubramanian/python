"""
python/01_Basics/built_in_sequence_functions_demo.py

Built-In Sequence Functions - Basics Demo:
    1. len(sequence)
    2. min(sequence), max(sequence)
    3. sum(sequence) for numeric sequences
    4. sorted(sequence)
    5. reversed(sequence)
    6. enumerate(sequence, start=0)
    7. zip(sequence1, sequence2, ...)
    8. any(sequence), all(sequence)
    9. list(), tuple(), str() conversions
    10. Useful combinations of built-ins
"""

# Sample sequences
# `numbers` is a list (mutable ordered sequence of integers).
numbers = [10, 4, 7, 2, 15]
# `letters` is a tuple (immutable ordered sequence of strings).
letters = ("a", "b", "c", "d")
# `word` is a string (ordered sequence of characters).
word = "python"

print("\nSample sequences:")
print(f"numbers -> {numbers}")
print(f"letters -> {letters}")
print(f"word    -> {word}")


# -----------------------------------------------------------------------------
# 1) len(sequence)
# -----------------------------------------------------------------------------
# `len()` returns the total number of elements in a sequence.
# For strings, each character is counted as one element.
print("\n1) len(sequence):")
print(f"len(numbers) -> {len(numbers)}")
print(f"len(letters) -> {len(letters)}")
print(f"len(word)    -> {len(word)}")


# -----------------------------------------------------------------------------
# 2) min(sequence), max(sequence)
# -----------------------------------------------------------------------------
# `min()` returns the smallest element in a sequence.
# `max()` returns the largest element in a sequence.
# For strings, comparison is lexicographic (alphabetical/Unicode order).
print("\n2) min(sequence), max(sequence):")
print(f"min(numbers) -> {min(numbers)}")
print(f"max(numbers) -> {max(numbers)}")
print(f"min(word)    -> {min(word)}")
print(f"max(word)    -> {max(word)}")


# -----------------------------------------------------------------------------
# 3) sum(sequence)
# -----------------------------------------------------------------------------
# sum() works for numeric sequences.
# It adds all numbers from left to right and returns one numeric total.
print("\n3) sum(sequence):")
print(f"sum(numbers) -> {sum(numbers)}")


# -----------------------------------------------------------------------------
# 4) sorted(sequence)
# -----------------------------------------------------------------------------
# sorted() always returns a NEW list.
# It does not modify the original sequence.
# `reverse=True` gives descending order.
print("\n4) sorted(sequence):")
print(f"sorted(numbers)                 -> {sorted(numbers)}")
print(f"sorted(numbers, reverse=True)   -> {sorted(numbers, reverse=True)}")
print(f"sorted(word)                    -> {sorted(word)}")
print(f"numbers (original unchanged)    -> {numbers}")


# -----------------------------------------------------------------------------
# 5) reversed(sequence)
# -----------------------------------------------------------------------------
# reversed() returns an iterator, so convert to list/tuple/string as needed.
# An iterator is a lazy object that gives one item at a time when consumed.
# That is why we wrap with list()/tuple() or join for display/use.
print("\n5) reversed(sequence):")
print(f"list(reversed(numbers)) -> {list(reversed(numbers))}")
print(f"tuple(reversed(letters)) -> {tuple(reversed(letters))}")
print(f"''.join(reversed(word))  -> {''.join(reversed(word))}")


# -----------------------------------------------------------------------------
# 6) enumerate(sequence, start=0)
# -----------------------------------------------------------------------------
# `enumerate()` pairs each element with an index.
# By default index starts at 0; here we start from 1 for human-friendly output.
print("\n6) enumerate(sequence):")
for index, value in enumerate(numbers, start=1):
    print(f"index={index}, value={value}")


# -----------------------------------------------------------------------------
# 7) zip(sequence1, sequence2, ...)
# -----------------------------------------------------------------------------
# `zip()` combines elements from multiple sequences position by position.
# It stops at the shortest input sequence length.
names = ["Asha", "Ben", "Chris"]
scores = [91, 84, 88]

print("\n7) zip(sequence1, sequence2, ...):")
paired = list(zip(names, scores))
print(f"names  -> {names}")
print(f"scores -> {scores}")
print(f"zip result -> {paired}")


# -----------------------------------------------------------------------------
# 8) any(sequence), all(sequence)
# -----------------------------------------------------------------------------
# `any()` returns True if at least one element is truthy.
# `all()` returns True only if every element is truthy.
flags_1 = [False, False, True]
flags_2 = [True, True, True]

print("\n8) any(sequence), all(sequence):")
print(f"any({flags_1}) -> {any(flags_1)}")
print(f"all({flags_1}) -> {all(flags_1)}")
print(f"any({flags_2}) -> {any(flags_2)}")
print(f"all({flags_2}) -> {all(flags_2)}")


# -----------------------------------------------------------------------------
# 9) list(), tuple(), str() conversions
# -----------------------------------------------------------------------------
# `list()` converts an iterable/sequence into a list.
# `tuple()` converts an iterable/sequence into a tuple.
# `str()` converts an object to its string representation.
print("\n9) Sequence conversions:")
print(f"list(letters)      -> {list(letters)}")
print(f"tuple(numbers)     -> {tuple(numbers)}")
print(f"str([1, 2, 3])     -> {str([1, 2, 3])}")


# -----------------------------------------------------------------------------
# 10) Useful combinations of built-ins
# -----------------------------------------------------------------------------
print("\n10) Useful combinations:")

# Combine zip + sorted to rank students by score (highest first).
# `zip(scores, names)` creates (score, name) pairs.
# `sorted(..., reverse=True)` sorts by first element of each tuple (score), descending.
ranked = sorted(zip(scores, names), reverse=True)
print(f"sorted(zip(scores, names), reverse=True) -> {ranked}")

# Combine enumerate + zip to show position with paired values.
# This gives structure: (rank_index, (name, score)).
indexed_pairs = list(enumerate(zip(names, scores), start=1))
print(f"list(enumerate(zip(names, scores), start=1)) -> {indexed_pairs}")

# Combine reversed + list for a concrete reversed sequence.
# Useful when you need actual indexable reversed data, not just an iterator.
reversed_numbers = list(reversed(numbers))
print(f"list(reversed(numbers)) -> {reversed_numbers}")

# Combine any/all with generator expressions for conditions.
# Generator expression computes values lazily without creating a full list in memory.
all_positive = all(n > 0 for n in numbers)
any_above_90 = any(score > 90 for score in scores)
print(f"all(n > 0 for n in numbers)   -> {all_positive}")
print(f"any(score > 90 for score in scores) -> {any_above_90}")
