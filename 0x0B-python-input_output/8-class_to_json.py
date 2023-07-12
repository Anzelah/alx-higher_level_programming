#!/usr/bin/python3
"""Defines a module."""


def class_to_json(obj):
    """Function to return dictionary description."""
    my_dict = {}

    if isinstance(obj, dict):
        my_dict = obj
    elif hasattr(obj, "__dict__"):
        my_dict = obj.__dict__

    return my_dict
