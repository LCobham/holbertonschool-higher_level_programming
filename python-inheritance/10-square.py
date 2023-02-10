#!/usr/bin/python3
"""
    This module defines a class Square that inherits from
    the class Retangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for a square"""
    def __init__(self, size):
        if BaseGeometry.integer_validator(self, "size", size) is None:
            Rectangle.__init__(self, size, size)
