#!/usr/bin/python3
"""Search and updates."""


def append_after(filename="", search_string="", new_string=""):
    """Function to insert a text after a specific string."""
    with open(filename, encoding="utf=8") as f:
        get_line = f.readlines()

    with open(filename, 'a', encoding="utf-8") as f:
        for line in get_line:
            if search_string:
                f.write(new_string)
