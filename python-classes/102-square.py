#!/usr/bin/python3
"""Creates a Square class.

Objects of type square only have a size attribute. Size has to be >= 0.
Are of the square can be obtained with the area method.
"""


class Square:
    """Square class.

    Attributes:
        size: size of square (must be positive int)
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculate the area of the square object"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __lt__(self, other):
        """Determine if a square's size is lesser than another."""
        return self.size < other.size

    def __le__(self, other):
        """Determine if a square's size is lesser or equal to another."""
        return self.size <= other.size

    def __eq__(self, other):
        """Determine if a square's size is equal another."""
        return self.size == other.size

    def __ne__(self, other):
        """Determine if a square's size is not equal to another's."""
        return self.size != other.size

    def __gt__(self, other):
        """Determine if a square's size is greater than another."""
        return self.size > other.size

    def __ge__(self, other):
        """Determine if a square's size is greater or equal to another."""
        return self.size >= other.size
