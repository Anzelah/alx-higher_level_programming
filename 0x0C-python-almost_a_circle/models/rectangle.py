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
        self.validate_setters("width", value)
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.validate_setters("height", value)
        self.__height = value

    @property
    def x(self):
        """Retrieve private attribute x of rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set private attribute x of rectangle."""
        self.validate_setters("x", value)
        self.__x = value

    @property
    def y(self):
        """Retrieve private attribute y of rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set private attribute y of rectangle."""
        self.validate_setters("y", value)
        self.__y = value

    @staticmethod
    def validate_setters(attribute, value):
        """Validate all setter methods and instantiation."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer" .format(attribute))
        if attribute == "height" or attribute == "width":
            if value <= 0:
                raise ValueError("{} must be > 0" .format(attribute))
        elif attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0" .format(attribute))
