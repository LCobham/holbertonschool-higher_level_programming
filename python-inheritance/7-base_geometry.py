#!/usr/bin/python3
"""
    This module creates the BaseGeometry class
"""


class BaseGeometry:
    """Class for basic geometry operations"""

    def area(self):
        """Raises an exception - not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed as an argument"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
