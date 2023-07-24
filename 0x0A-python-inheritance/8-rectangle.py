#!/usr/bin/python3
"""Defines a module."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import a module."""


class Rectangle(BaseGeometry):
    """Create a new class inheriting from basegeometry."""

    def __init__(self, width, height):
        """Initialize the class."""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
