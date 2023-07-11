#!/usr/bin/python3
"""Defines a module."""


def write_file(filename="", text=""):
    """Function to write to a file."""
    with open(filename, 'w', encoding="utf-8") as f:
        written_chars = f.write(text)
    return written_chars
