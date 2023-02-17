#!/usr/bin/python3
"""
    This module defines the Rectangle class.
"""

from random import randrange
from models.base import Base


class Rectangle(Base):
    """Rectangle class.

    Attributes:
        width: (int) width of rectangle
        height: (int) height of rectangle
        x: (int) number of spaces printed on each line before Rectangle
        y: (int) number of newlines printed before printing Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Calculates the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
            Prints the rectangle using the '#' symbol
        """
        print('\n' * self.y, end='')
        for h in range(self.height):
            print("{}{}".format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """Tidy print of Rectangle object"""
        return "{} ({}) {}/{} - {}/{}".format(
            "[Rectangle]", self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
            Update the value of a rectangle
        """
        attrNames = ['id', 'width', 'height', 'x', 'y']

        if args:
            for key, value in zip(attrNames, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Return the dictionary representation of a Rectangle
        """
        my_dic = dict()
        for key in ['id', 'width', 'height', 'x', 'y']:
            my_dic[key] = getattr(self, key)

        return my_dic

    @classmethod
    def createRandomRectangle(cls):
        return cls(randrange(1, 100), randrange(1, 100), randrange(1, 100),
                   randrange(1, 100), randrange(1, 100))
