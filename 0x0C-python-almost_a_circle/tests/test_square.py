#!/usr/bin/python3
import unittest
from models.square import Square
"""Import modules."""


class test_square(unittest.TestCase):
    """Initialize square instance with its size."""

    def test_id(self):
        """Test id."""
        self.assertEqual(Square(5, 2, 3, 4).id, 4)

    def test_width(self):
        """Test the width."""
        self.assertEqual(Square(5).size, 5)

    def test_height(self):
        """Test the height."""
        self.assertEqual(Square(5).size, 5)

    def test_coordinates(self):
        """Test the x and y coordinates."""
        self.assertEqual(Square(5, 0, 0, 2).x, 0)
        self.assertEqual(Square(5, 1, 2, 10).y, 2)

    def test_exception(self):
        """Raise TypeError."""
        with self.assertRaises(TypeError):
            s = Square("string")

    def test_negative(self):
        """Test negative digit."""
        with self.assertRaises(ValueError):
            s = Square(-4)


if __name__ == '__main__':
    unittest.main()
