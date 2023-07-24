#!/usr/bin/python3
"""Defines a module."""


Rectangle = __import__('9-rectangle').Rectangle
"""Imports a module."""


class Square(Rectangle):
    """Create a new class inheriting from Rectangle created before."""

    def __init__(self, size):

        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):

        return self.__size * self.__size
