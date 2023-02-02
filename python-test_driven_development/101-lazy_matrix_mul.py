#!/usr/bin/python3
"""
    Multiply matrices using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    return numpy.matmul(m_a, m_b)
