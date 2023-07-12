#!/usr/bin/python3
"""Write a class Student."""


class Student:
    """A new class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation."""

        if isinstance(self, dict):
            return self
        elif hasattr(self, "__dict__"):
            return self.__dict__
