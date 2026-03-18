"""
More simple examples of exception types in Python.
"""


def handle_assertion_error():
    try:
        number = -5
        assert number > 0, "Number must be positive"
        return "Valid number"
    except AssertionError:
        return "AssertionError: number is not positive"


def handle_module_not_found_error():
    try:
        import not_a_real_module
        return not_a_real_module
    except ModuleNotFoundError:
        return "ModuleNotFoundError: module does not exist"


def handle_permission_error():
    try:
        raise PermissionError("You do not have permission")
    except PermissionError:
        return "PermissionError: access denied"


def handle_runtime_error():
    try:
        raise RuntimeError("Something went wrong while running")
    except RuntimeError:
        return "RuntimeError: program error happened"


def handle_not_implemented_error():
    try:
        raise NotImplementedError("This part is not ready yet")
    except NotImplementedError:
        return "NotImplementedError: feature not ready"


def handle_eof_error():
    try:
        raise EOFError("No more input")
    except EOFError:
        return "EOFError: input ended"


if __name__ == "__main__":
    print("1. AssertionError")
    print(handle_assertion_error())

    print("\n2. ModuleNotFoundError")
    print(handle_module_not_found_error())

    print("\n3. PermissionError")
    print(handle_permission_error())

    print("\n4. RuntimeError")
    print(handle_runtime_error())

    print("\n5. NotImplementedError")
    print(handle_not_implemented_error())

    print("\n6. EOFError")
    print(handle_eof_error())
