#!/usr/bin/python3
"""A class square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the subclass."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overide the str method."""
        return ("Square] ({}) {}/{} - {}" .format(self.id, self.x,
                self.y, self.width))
