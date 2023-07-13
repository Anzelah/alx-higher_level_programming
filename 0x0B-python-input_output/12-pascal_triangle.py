#!/usr/bin/python3
"""Returns a list representing the pascal triangle."""


def pascal_triangle(n):
    """Defines a function to return pascal triangle."""
    new_list = []
    if  n <= 0:
        new_list = []
    else:
        for i in range(n):


