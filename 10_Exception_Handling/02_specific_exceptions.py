"""
Handling specific exceptions and avoiding bare except.
"""

def read_lines(path):
    """Read lines from a file, handling common errors."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return [f"File not found: {path}"]
    except PermissionError:
        return [f"No permission to read: {path}"]


def get_item(items, index):
    """Safely get an item from a list."""
    try:
        return items[index]
    except IndexError:
        return f"Index {index} is out of range"


def to_float(text):
    """Convert text to float, raising on invalid input."""
    try:
        return float(text)
    except ValueError as exc:
        # Re-raise with a clearer message
        raise ValueError(f"'{text}' is not a valid float") from exc


if __name__ == "__main__":
    print("Example 1: read_lines")
    for line in read_lines("missing.txt"):
        print(line)

    print("\nExample 2: get_item")
    print(get_item(["a", "b", "c"], 1))
    print(get_item(["a", "b", "c"], 5))

    print("\nExample 3: to_float with explicit error")
    try:
        print(to_float("3.14"))
        print(to_float("pi"))
    except ValueError as e:
        print("Caught error:", e)
