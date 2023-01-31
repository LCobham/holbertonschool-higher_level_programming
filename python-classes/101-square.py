#!/usr/bin/python3
"""Creates a Square class.

Objects of type square only have a size attribute. Size has to be >= 0.
Are of the square can be obtained with the area method.
"""


class Square:
    """Square class.

    Attributes:
        size: size of square (must be positive int)
        position: tuple of two positive ints.
        First element is n of spaces in each line when printing square.
        Second element is n of newlines before printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0] and position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """Calculate the area of the square object"""
        return self.__size ** 2

    def my_print(self):
        """Print a square using # symbols."""
        if self.size == 0:
            print("")
            return

        for j in range(self.position[1]):
            print("")
        for i in range(self.size):
            print("{}{}".format(' ' * self.position[0], "#" * self.size))

    def __str__(self):
        """Print a square using # symbols.

        Return: The str to be printed on the last line.
        """
        if self.size == 0:
            return ""
        for j in range(self.position[1]):
            print("")
        for i in range(self.size - 1):
            print("{}{}".format(' ' * self.position[0], "#" * self.size))

        return "{}{}".format(' ' * self.position[0], "#" * self.size)
