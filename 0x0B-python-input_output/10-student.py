#!/usr/bin/python3
"""Write a class Student."""


class Student:
    """A new class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict representation."""

        if attrs is list:
            return attrs.list
        elif hasattr(self, "__dict__"):
           return self.__dict__

