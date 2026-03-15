"""
Using context managers and cleanup patterns.
"""

from contextlib import contextmanager


@contextmanager
def open_safe(path, mode):
    """A simple context manager that wraps open()."""
    f = None
    try:
        f = open(path, mode, encoding="utf-8")
        yield f
    finally:
        if f is not None:
            f.close()


def write_and_read(path, text):
    """Write text then read it back safely."""
    try:
        with open_safe(path, "w") as f:
            f.write(text)
        with open_safe(path, "r") as f:
            return f.read()
    except OSError as exc:
        return f"File error: {exc}"


def cleanup_example(items):
    """Demonstrate cleanup in a finally block."""
    resource = []
    try:
        for item in items:
            if item == "bad":
                raise ValueError("bad item found")
            resource.append(item)
        return f"Processed: {resource}"
    except ValueError as exc:
        return f"Failed: {exc}"
    finally:
        resource.clear()  # cleanup


if __name__ == "__main__":
    print("Example 1: write_and_read")
    print(write_and_read("temp_note.txt", "Hello"))

    print("\nExample 2: cleanup_example")
    print(cleanup_example(["a", "b"]))
    print(cleanup_example(["a", "bad", "c"]))
