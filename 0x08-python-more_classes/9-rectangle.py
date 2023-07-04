#!/usr/bin/python3
""" Defines a class rectangle. """


class Rectangle:
    """ Represents a rectangle. """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the rectangle.
        Define the rectangle attributes/variables."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        "Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Find the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Creates a static method that calls another method area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        area_of_1 = rect_1.area()
        area_of_2 = rect_2.area()
        if area_of_1 >= area_of_2:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a class method square in the class Rectangle."""
        return cls(size, size)

    def __str__(self):
        """Create a new string of given object."""
        if self.__height == 0 or self.__width == 0:
            return ""

        rstr = ""
        for _ in range(self.__height):
            rstr += str(self.print_symbol) * self.__width + '\n'
        rstr = rstr.strip()  # removes extra newline after printing

        return rstr

    def __repr__(self):
        """Return a string representation of the rectangle."""
        str_rep = f'Rectangle({self.width}, {self.height})'

        return str_rep

    def __del__(self):
        """Ensures deletion of an instance Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
