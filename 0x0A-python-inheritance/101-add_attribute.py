#!/usr/bin/python3
"""Defines a module."""


def add_attribute(obj, name, value):
    """Function that adds an attribute."""

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
