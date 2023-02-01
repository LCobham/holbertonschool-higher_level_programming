#!/usr/bin/python3
"""
    This module defines a function to print a square (using '#')
    of variable size.
"""


def print_square(size):
    """Print a square using '#'."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format('#' * size))
