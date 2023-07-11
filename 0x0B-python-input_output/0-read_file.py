#!/usr/bin/python3
""" Defines the module."""


def read_file(filename=""):
    """Function for reading the file."""
    with open('my_file_0.txt', encoding="utf-8") as f:
        print(f.read(), end="")
