#!/usr/bin/python3
"""
    This module creates the BaseGeometry clas.
    It also creates the Reclangle class, which inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines an object for a rectangle"""
    def __init__(self, width, height):
        """
            Checks if width & heigh are valid integers and assigns them
            as private instance attributes
        """
        if BaseGeometry.integer_validator(self, "width", width) is None:
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height) is None:
            self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
