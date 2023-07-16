#!/usr/bin/python3
"""A class square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the subclass."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the width of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overide the str method."""
        return ("Square] ({}) {}/{} - {}" .format(self.id, self.x,
                self.y, self.width))
