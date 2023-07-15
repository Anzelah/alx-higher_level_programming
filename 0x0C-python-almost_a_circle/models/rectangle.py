#!/usr/bin/python3
"""Class rectangle."""
from models.base import Base


class Rectangle(Base):
    """Create a class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the subclass."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Retrieve private attribute x of rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the width of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """Retrieve the width of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the width of the rectangle."""
        self.__y = value
