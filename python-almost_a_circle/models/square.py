#!/usr/bin/python3
"""
    This module defines the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class.

    Attributes:
        size: (int) square size
        x: (int) number of spaces printed on each line before Square
        y: (int) number of newlines printed before printing Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    def __str__(self):
        """
            Tidy print of Square object
        """
        return "{} ({}) {}/{} - {}".format(
            "[Square]", self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
            Update the value of a square
        """
        attrNames = ['id', 'size', 'x', 'y']

        if args:
            for key, value in zip(attrNames, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Return the dictionary representation of a Square
        """
        my_dic = dict()
        for key in ['id', 'size', 'x', 'y']:
            my_dic[key] = getattr(self, key)

        return my_dic
