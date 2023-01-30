#!/usr/bin/python3
"""Creates a Square class.

Objects of type square only have a size attribute. Are of the square can be
obtained with the area method
"""


class Square:
    """Creates a square

    Attributes:
        size: integer indicating the size of the square
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """Calculate the area of a square."""
        return self.__size ** 2
