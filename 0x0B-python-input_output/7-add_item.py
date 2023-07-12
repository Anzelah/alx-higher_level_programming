#!/usr/bin/python3
"""Defines a module."""


import json
import sys
"""Imports a module."""

python_list = []


def save_to_json_file(my_obj, filename):
    """A function to write an object to text file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Function to create an object from a json file."""
    with open(filename, encoding="utf-8") as f:
        obj = json.load(f)
    return obj

    try:
        python_list = load_from_json_file("add_item.json")
    except Exception:
        pass


another_list = sys.argv[1:]
new_list = python_list + another_list
save_to_json_file(new_list, "add_item.json")
