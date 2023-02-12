#!/usr/bin/python3
"""
    This module defines a function to print pascal's triangle up
    to the n-th level
"""


def pascal_triangle(n):
    """Return a list with the first n rows of Pascal's triangle"""
    if n <= 0:
        return []

    final, initial = [], [0, 1, 0]
    for i in range(n):
        final.append(initial[1:-1])
        new = [initial[i] + initial[i + 1] for i in range(len(initial) - 1)]
        initial = [0] + new + [0]

    return final
