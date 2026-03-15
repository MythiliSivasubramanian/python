"""
Custom exceptions and practical patterns.
"""

class InvalidAgeError(Exception):
    """Raised when age is out of allowed range."""


def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 120:
        raise InvalidAgeError("age must be between 0 and 120")
    return True


def safe_write(path, text):
    """Write text to a file and guarantee close with a context manager."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        return f"Write failed: {exc}"
    return "Write successful"


if __name__ == "__main__":
    print("Example 1: validate_age")
    for sample in [25, -1, 200, "30"]:
        try:
            validate_age(sample)
            print(sample, "is valid")
        except (InvalidAgeError, TypeError) as e:
            print(sample, "is invalid:", e)

    print("\nExample 2: safe_write")
    print(safe_write("example_output.txt", "Hello, exceptions!"))
