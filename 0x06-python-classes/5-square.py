#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """ Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.
        Define the square attributes/variables."""

        self.__size = size

    @property
    def size(self):
        """Retrieve the size of square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Define the square capabilities."""
        return self.__size * self.__size

    def my_print(self):
        """Print square to stdout with character #"""

        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)
