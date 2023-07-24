#!/usr/bin/python3
"""Defines a module."""


class MyInt(int):
    """Create a new class."""

    def __init__(self, number):
        self.number = number

    def __ne__(self, value):
        return (self.number == value)

    def __eq__(self, value):
        return (self.number != value)
