"""
Exception hierarchy and catching multiple exceptions.
"""

def convert_and_divide(a_text, b_text):
    """Convert inputs to ints and divide."""
    try:
        a = int(a_text)
        b = int(b_text)
        return a / b
    except (ValueError, ZeroDivisionError) as exc:
        return f"Error: {exc}"


def risky_operation(value):
    """Show how a general Exception catch can be used sparingly."""
    try:
        if value == "key":
            raise KeyError("Missing expected key")
        if value == "type":
            raise TypeError("Wrong type provided")
        return "All good"
    except Exception as exc:
        # Catching Exception is OK here for a top-level guard
        return f"Caught: {type(exc).__name__}: {exc}"


if __name__ == "__main__":
    print("Example 1: convert_and_divide")
    print(convert_and_divide("10", "2"))
    print(convert_and_divide("ten", "2"))
    print(convert_and_divide("10", "0"))

    print("\nExample 2: risky_operation")
    print(risky_operation("key"))
    print(risky_operation("type"))
    print(risky_operation("ok"))
