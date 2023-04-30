#!/usr/bin/python3
"""2-matrix_divided.py
    This module contains a function 'matrix_divided'
    you can test the function with the command

    python3 -m doctest -v ./test/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """Divides a matrix with given value
    Args:
    matrix (list): 2d list
    div: int / float
    """
    if (isinstance(matrix, list) is False
            or all(isinstance(elem, list) for elem in matrix) is False
            or all(all(isinstance(elem, (int, float)) for elem in row)
                   for row in matrix) is False):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) != 0:
        size = len(matrix[0])
        for elem in matrix:
            if len(elem) != size:
                raise TypeError("Each row of the matrix must have"
                                " the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(box / div, 2) for box in row] for row in matrix])
