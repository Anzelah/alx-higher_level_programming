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

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        "Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Find the perimeter of the rectangle."""

        return (self.__width + self.__height) * 2

        width = 0
        height = 0
        if width == 0 or height == 0:
            return 0
