"""
Exception Handling Basics: try/except/else/finally
"""

def safe_divide(a, b):
    """Return a / b, or a message if division is invalid."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result
    finally:
        # This always runs, even if an exception occurred
        pass


def parse_int(text):
    """Convert text to int, showing a friendly error."""
    try:
        return int(text)
    except ValueError:
        return f"'{text}' is not a valid integer"


if __name__ == "__main__":
    print("Example 1: safe_divide")
    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

    print("\nExample 2: parse_int")
    print("'42' ->", parse_int("42"))
    print("'abc' ->", parse_int("abc"))

    print("\nExample 3: try/except/else structure")
    try:
        value = int("100")
    except ValueError:
        print("Could not convert")
    else:
        print("Converted value:", value)
    finally:
        print("Cleanup step (always runs)")
