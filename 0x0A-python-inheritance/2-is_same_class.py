#!/usr/bin/python3
"""Defines a module."""


def is_same_class(obj, a_class):
    """Returns True or false depending on whether
    object is instance of class."""

    if type(obj) is a_class:
        return True
    else:
        return False
