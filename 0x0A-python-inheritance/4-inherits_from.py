#!/usr/bin/python3
"""Defines a module."""


def inherits_from(obj, a_class):
    """Function to check if object is an instance of a class
    that inherited from the specified subclass."""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
