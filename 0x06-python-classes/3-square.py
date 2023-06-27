#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """ Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.
        Define the square attributes/variables."""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Define the square capabilities."""
        return self.__size * self.__size
