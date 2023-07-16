#!/usr/bin/python3
"""Defines a module."""


import json
"""Imports a module."""


class Base:
    """Create aclass base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json list representation of list dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
