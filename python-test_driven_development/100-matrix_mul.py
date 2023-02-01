#!/usr/bin/python3
"""
    This module writes a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices together."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    aLen = len(m_a)
    for i in range(aLen):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")

    if aLen == 0 or (aLen == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    aFirstRowLen = len(m_a[0])

    bLen = len(m_b)
    for i in range(bLen):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
    if bLen == 0 or (bLen == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    bFirstRowLen = len(m_b[0])

    if not all(len(m_a[i]) == aFirstRowLen for i in range(aLen)):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[i]) == bFirstRowLen for i in range(bLen)):
        raise TypeError("each row of m_b must be of the same size")

    if not all(type(m_a[i][j]) is not int or float
               for i in range(aLen) for j in range(aFirstRowLen)):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(m_b[i][j]) is int or float
               for i in range(bLen) for j in range(bFirstRowLen)):
        raise TypeError("m_b should contain only integers or floats")

    if bLen != aFirstRowLen:
        raise ValueError("m_a and m_b can't be multiplied")

    ReturnMatrix = []
    for i in range(aLen):
        rowList = []
        for m in range(bFirstRowLen):
            res = 0
            for j in range(bLen):
                res += m_a[i][j] * m_b[j][m]
            rowList.append(res)
        ReturnMatrix.append(rowList)

    return ReturnMatrix
