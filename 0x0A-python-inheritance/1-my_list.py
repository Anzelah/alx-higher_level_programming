#!/usr/bin/python3
"""Defines a module."""


class MyList(list):
    """Create a class which inhertes from another class."""


    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
