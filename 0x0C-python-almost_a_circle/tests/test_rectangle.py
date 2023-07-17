#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Import modules."""


class Test_rectangle(unittest.TestCase):
    """Initialize square instance with its size."""

    def test_id(self):
        """Test the id."""
        self.assertEqual(Rectangle(10, 5, 2, 3, 1).id, 1)

    def test_width(self):
        """Test the width."""
        self.assertEqual(Rectangle(5, 1, 2, 9).width, 5)

    def test_height(self):
        """Test the height."""
        self.assertEqual(Rectangle(5, 10, 2, 10).height, 10)

    def test_coordinates(self):
        """Test the x and y coordinates."""
        self.assertEqual(Rectangle(5, 4, 3, 8, 2).x, 3)
        self.assertEqual(Rectangle(5, 1, 2, 4, 10).y, 4)

    def test_exception(self):
        """Raise TypeError."""
        with self.assertRaises(TypeError):
            s = Rectangle("string")

    def test_negative(self):
        """Test negative digit."""
        with self.assertRaises(ValueError):
            s = Rectangle(-4, -5)


if __name__ == '__main__':
    unittest.main()
