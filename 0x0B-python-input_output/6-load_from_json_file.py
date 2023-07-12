#!/usr/bin/python3
"""Defining a module."""

import json
"""Import module."""


def load_from_json_file(filename):
    """Function to create an object from a json file."""
    with open(filename, encoding="utf-8") as f:
        obj = json.load(f)
    return obj
