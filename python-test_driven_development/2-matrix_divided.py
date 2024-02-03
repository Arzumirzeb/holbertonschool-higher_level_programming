#!/usr/bin/python3
"""Define function for divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides elemens of a matrix"""
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
