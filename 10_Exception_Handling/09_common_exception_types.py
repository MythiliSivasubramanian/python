"""
Simple examples of common exception types in Python.
"""


def handle_zero_division():
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError:
        return "ZeroDivisionError: cannot divide by zero"


def handle_value_error():
    try:
        number = int("hello")
        return number
    except ValueError:
        return "ValueError: invalid value for int()"


def handle_type_error():
    try:
        result = 5 + "10"
        return result
    except TypeError:
        return "TypeError: cannot add int and str"


def handle_index_error():
    try:
        colors = ["red", "blue"]
        return colors[5]
    except IndexError:
        return "IndexError: list index out of range"


def handle_key_error():
    try:
        student = {"name": "Mythili", "age": 21}
        return student["mark"]
    except KeyError:
        return "KeyError: key not found in dictionary"


def handle_name_error():
    try:
        return total_marks
    except NameError:
        return "NameError: variable is not defined"


def handle_attribute_error():
    try:
        number = 25
        return number.append(10)
    except AttributeError:
        return "AttributeError: object has no such method"


def handle_file_not_found_error():
    try:
        with open("missing_file.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "FileNotFoundError: file does not exist"


def try_except_else_finally_demo(text):
    try:
        value = int(text)
    except ValueError:
        return "except block: not a valid number"
    else:
        print("else block: conversion successful")
        return value
    finally:
        print("finally block: always runs")


if __name__ == "__main__":
    print("1. ZeroDivisionError")
    print(handle_zero_division())

    print("\n2. ValueError")
    print(handle_value_error())

    print("\n3. TypeError")
    print(handle_type_error())

    print("\n4. IndexError")
    print(handle_index_error())

    print("\n5. KeyError")
    print(handle_key_error())

    print("\n6. NameError")
    print(handle_name_error())

    print("\n7. AttributeError")
    print(handle_attribute_error())

    print("\n8. FileNotFoundError")
    print(handle_file_not_found_error())

    print("\n9. try / except / else / finally")
    print(try_except_else_finally_demo("50"))
    print(try_except_else_finally_demo("abc"))
