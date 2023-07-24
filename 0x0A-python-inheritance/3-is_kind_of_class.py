#!/usr/bin/python3
"""Defines a module."""


def is_kind_of_class(obj, a_class):
    """Function to check for object instance or inheritance."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
