#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """ Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.
        Define the square attributes/variables."""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of square."""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute of the square."""

        if (not isinstance(value, tuple) or len(value) != 2 or
                any(not isinstance(num, int) or num < 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Calculate the area of a square.."""

        return self.__size * self.__size

    def my_print(self):
        """Print square to stdout with character #"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
