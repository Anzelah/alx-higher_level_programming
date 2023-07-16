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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle instance with character #."""

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """Overide the str method."""
        return ("[Rectangle] ({}) {}/{} - {}/{}" .format(self.id, self.x,
                self.y, self.width, self.height))

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

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of the class."""

        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
