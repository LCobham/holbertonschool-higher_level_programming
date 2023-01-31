#!/usr/bin/python3
"""
    This module creates a function to add two numbers.
"""


def add_integer(a, b=98):
    """Adds two numbers (ints). The function accepts floats, but will cast
    them as integers before returning.

    Args:
        a (int / float): first integer to add
        b (int / float): second int to add. Defaults to 98.

    Return:
        int: a + b

    Raises:
        TypeError: if a or b aren't ints nor floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    res = int(a) + int(b)
    return res
