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

    def my_print(self):
        """Print a square using # symbols."""
        if self.size == 0:
            print("")
            return

        for i in range(self.size):
            print("{}".format("#" * self.size))
