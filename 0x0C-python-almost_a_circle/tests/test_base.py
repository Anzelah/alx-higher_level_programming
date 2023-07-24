#!/usr/bin/python3
"""Create your own test."""


import unittest
from models.base import Base
"""Import a unittest module."""


class test_base(unittest.TestCase):
    """Base unittests."""

    def test_id(self):
        """Test id."""
        self.assertEqual(Base(10).id, 10)

    def none_id(self):
        """Check if id not none."""
        self.assertEqual(Base().id, 1)

    def check_neg_id(self):
        """If id is a negative number."""
        self.assertEqual(Base(-20).id, -20)

    def check_zero_id(self):
        """If id is zero"""
        self.assertEqual(Base(0).id, 0)

    def check_string_id(self):
        """If id is a string"""
        self.assertEqual(Base("Trent").id, "Trent")


if __name__ == '__main__':
    unittest.main()
