#!/usr/bin/python3
"""
    This module defines a function to devide all elements
    of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given number."""

    unaccepted = (float('nan'), float('inf'), -float('inf'))
    if not isinstance(div, (int, float)) or div in unaccepted:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists (of same length)")

    newMatrix = []
    matLength = len(matrix)

    if matLength > 0:
        if isinstance(matrix[0], list):
            firstRowLength = len(matrix[0])
        else:
            raise TypeError("elements of matrix aren't lists")
    else:
        return newMatrix

    newMatrix = [matrix[i].copy() for i in range(matLength)]

    for i in range(matLength):
        row = newMatrix[i]
        if not isinstance(row, list):
            raise TypeError("elements of matrix aren't lists")
        rowLength = len(row)
        if rowLength != firstRowLength:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(rowLength):
            if not isinstance(row[j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
            else:
                row[j] = round(row[j] / div, 2)

    return newMatrix
