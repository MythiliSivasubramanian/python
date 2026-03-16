"""
Basic assertions (simple checks while learning).
"""

def average(values):
    """Compute average; assert list is not empty."""
    assert len(values) > 0, "values must not be empty"
    return sum(values) / len(values)


if __name__ == "__main__":
    print("Example: average")
    print(average([2, 4, 6]))

    print("\nExample: assertion error")
    try:
        print(average([]))
    except AssertionError as e:
        print("Caught:", e)
