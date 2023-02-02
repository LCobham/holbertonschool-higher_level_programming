#!/usr/bin/python3
"""
    This module defines a class for a rectangle
"""


class Rectangle:
    """Defines a rectangle object.

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Return the rectangle as a string"""
        if self.width == 0 or self.height == 0:
            return ''
        li = ["{}".format("#" * self.width) for i in range(self.height)]
        return "\n".join(li)

    def __repr__(self):
        """Returns a formal string representation of the object.
        Object can be recreated using eval()
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def area(self):
        """Calculate thearea of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * self.height + 2 * self.width
