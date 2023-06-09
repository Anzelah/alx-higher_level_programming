#!/usr/bin/python3
"""Define class MagicClass matching bytecode provided."""

import math
"""import module fo math operations."""


class MagicClass:
    """Defines a circle."""

    def __init__(self, radius=0):
        "Initialize magicclass."""

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Find the area of magicclass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Find the circumference of magicclass."""
        return (self.__radius * math.pi * 2)
