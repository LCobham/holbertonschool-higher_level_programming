#!/usr/bin/python3
"""Create a Square class.

This module creates an empty class called Square. Squares only have
a size attribute and no methods.
"""


class Square:
    """Create the Square class.

    Args:
        size: size of square.
    """
    def __init__(self, size):
        self.__size = size
