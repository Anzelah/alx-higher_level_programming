#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """ Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.
        Set the size of the square"""

        try:
            int(size)
            if size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')

        self.__size = size