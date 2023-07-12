#!/usr/bin/python3
"""Defines a module."""


import sys
"""Imports a module."""


python_list = []

if __name__ == "__main__":
    """Function to import code as script."""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        python_list = load_from_json_file("add_item.json")
    except Exception:
        python_list = []


another_list = sys.argv[1:]
new_list = python_list + another_list
save_to_json_file(new_list, "add_item.json")
