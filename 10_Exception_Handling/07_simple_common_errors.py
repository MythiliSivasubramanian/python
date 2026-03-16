"""
examples of common errors.
"""

def get_list_item(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index out of range"


def get_dict_value(data, key):
    try:
        return data[key]
    except KeyError:
        return "Key not found"


if __name__ == "__main__":
    print("List example:")
    print(get_list_item(["a", "b"], 0))
    print(get_list_item(["a", "b"], 5))

    print("\nDict example:")
    print(get_dict_value({"name": "Asha"}, "name"))
    print(get_dict_value({"name": "Asha"}, "age"))
