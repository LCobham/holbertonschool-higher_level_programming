#!/usr/bin/python3
"""
    This module creates the BaseGeometry clas.
    It also creates the Reclangle class, which inherits from BaseGeometry
"""


class BaseGeometry:
    """Class for basic geometry operations"""

    def area(self):
        """Raises an exception - not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed as an argument"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class defines an object for a rectangle"""
    def __init__(self, width, height):
        """
            Checks if width & heigh are valid integers and assigns them
            as private instance attributes
        """
        if super().integer_validator("width", width) is None:
            self.__width = width
        if super().integer_validator("height", height) is None:
            self.__height = height
