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

    @staticmethod
    def from_json_string(json_string):
        """A function to convert from json string to object."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json representation to a file."""

        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        data = []
        for objects in list_objs:
            objects = objects.to_dictionary()
            thejson_string = json.loads(cls.to_json_string(objects))
            data.append(thejson_string)

        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set."""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(10, 6)

        elif cls.__name__ == "Square":
            dummy_instance = cls(5)

        dummy_instance.update(**dictionary)

        return dummy_instance
