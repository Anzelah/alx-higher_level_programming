#!/usr/bin/python3
""" Defines a class rectangle. """


class Rectangle:
    """ Represents a rectangle. """
    def __init__(self, width=0, height=0):
        """Initialize the rectangle.
        Define the rectangle attributes/variables."""

        self.width = width
        self.height = height

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
        return self.__width * self.__height

    def perimeter(self):
        """Find the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Create a new string of given object."""
        if self.__height == 0 or self.__width == 0:
            return ""

        rstr = ""
        for _ in range(self.__height):
            rstr += '#' * self.__width + '\n'
        rstr = rstr.strip()  # removes extra newline after printing

        return rstr
