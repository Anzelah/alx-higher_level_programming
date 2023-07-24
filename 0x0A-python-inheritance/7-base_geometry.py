#!/usr/bin/python3
"""Defines a module."""


class BaseGeometry:
    """Create a new class."""

    def __init__(self):
        """Initialize the class."""
        pass

    def area(self):
        """Calculate the area."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate the value."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer" .format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
