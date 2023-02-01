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
    if aLen == 0 or (aLen == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    aFirstRowLen = len(m_a[0])

    bLen = len(m_b)
    if bLen == 0 or (bLen == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    bFirstRowLen = len(m_b[0])

    for i in range(aLen):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        rowLen = len(m_a[i])
        if aFirstRowLen != rowLen:
            raise TypeError("each row of m_a must be of the same size")
        for j in range(rowLen):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for i in range(bLen):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        rowLen = len(m_b[i])
        if bFirstRowLen != rowLen:
            raise TypeError("each row of m_b must be of the same size")
        for j in range(rowLen):
            if not isinstance(m_b[i][j], (int, float)):
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
