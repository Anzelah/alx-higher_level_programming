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
        return ("[Square] ({}) {}/{} - {}" .format(self.id, self.x,
                self.y, self.width))

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of the class."""

        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
