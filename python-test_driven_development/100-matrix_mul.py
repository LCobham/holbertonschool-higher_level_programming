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

    aLen, bLen = len(m_a), len(m_b)
    if not all(type(m_a[i]) is list for i in range(aLen)):
        raise TypeError("m_a must be a list of lists")
    if not all(type(m_b[i]) is list for i in range(bLen)):
        raise TypeError("m_b must be a list of lists")

    if aLen == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if bLen == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    aFirstRowLen, bFirstRowLen = len(m_a[0]), len(m_b[0])
    if not all(len(m_a[i]) == aFirstRowLen for i in range(aLen)):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[i]) == bFirstRowLen for i in range(bLen)):
        raise TypeError("each row of m_b must be of the same size")

    if not all(isinstance(m_a[i][j], (int, float))
               for i in range(aLen) for j in range(aFirstRowLen)):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(m_b[i][j], (int, float))
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
