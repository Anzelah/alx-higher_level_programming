#!/usr/bin/python3
"""Defines a module."""


def append_write(filename="", text=""):
    """Function to append to a file."""
    with open(filename, 'a', encoding="utf-8") as f:
        written_chars = f.write(text)
    return written_chars
