"""
Other simple exception examples in Python.
"""


def handle_import_error():
    try:
        raise ImportError("Problem while importing")
    except ImportError:
        return "ImportError: could not import"


def handle_os_error():
    try:
        raise OSError("Operating system error")
    except OSError:
        return "OSError: system related error"


def handle_memory_error():
    try:
        raise MemoryError("Not enough memory")
    except MemoryError:
        return "MemoryError: memory is full"


def handle_stop_iteration():
    try:
        numbers = iter([1, 2])
        next(numbers)
        next(numbers)
        next(numbers)
    except StopIteration:
        return "StopIteration: no more items in iterator"


def handle_unbound_local_error():
    try:
        def show_value():
            print(value)
            value = 10

        show_value()
    except UnboundLocalError:
        return "UnboundLocalError: local variable used before value is assigned"


def handle_keyboard_interrupt():
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        return "KeyboardInterrupt: program stopped by user"


if __name__ == "__main__":
    print("1. ImportError")
    print(handle_import_error())

    print("\n2. OSError")
    print(handle_os_error())

    print("\n3. MemoryError")
    print(handle_memory_error())

    print("\n4. StopIteration")
    print(handle_stop_iteration())

    print("\n5. UnboundLocalError")
    print(handle_unbound_local_error())

    print("\n6. KeyboardInterrupt")
    print(handle_keyboard_interrupt())
