#!/usr/bin/python3
""" Defines a class rectangle. """


class Rectangle:
    """ Represents a rectangle. """
    def __init__(self, width=0, height=0):
        """Initialize the rectangle.
        Define the rectangle attributes/variables."""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""

        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        "Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""

        self.__height = value
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
