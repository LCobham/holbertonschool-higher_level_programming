#!/usr/bin/python3
"""Creates a Square class.

Instances of the Square class only have a size, that defaults to 0.
No methods are available yet.
"""

class Square:
    """Creates an object of type Square.

    Args:
        size (int): size of the square. Must be greater than 0

    Raises:
        ValueError: if size < 0
        TypeError: if size isn't an int
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
