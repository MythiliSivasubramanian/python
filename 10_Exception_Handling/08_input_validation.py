"""
Simple input validation with ValueError.
"""

def validate_age(age):
    if age < 0:
        raise ValueError("age must be positive")
    if age > 120:
        raise ValueError("age must be realistic")
    return True


if __name__ == "__main__":
    for age in [10, -5, 200]:
        try:
            validate_age(age)
            print(age, "is valid")
        except ValueError as e:
            print(age, "is invalid:", e)
