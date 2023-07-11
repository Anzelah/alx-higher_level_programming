#!/usr/bin/python3
"""Define a module."""

import json
"""Imports a module."""


def save_to_json_file(my_obj, filename):
    """A function to write an object to text file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
