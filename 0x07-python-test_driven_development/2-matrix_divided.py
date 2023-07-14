#!/usr/bin/python3
"""Divide a matrix."""


def matrix_divided(matrix, div):
    """Function to divide each element inside a matrix."""
    if not isinstance(matrix, (int, float)):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if not equal:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] / div
            result = matrix[i][j]

    result(round(i) for i in range(2))
    new_matrix = result.append

