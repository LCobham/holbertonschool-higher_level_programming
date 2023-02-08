#!/usr/bin/python3
"""
    This module defines a function to check is an object belongs
    to a subclass of the given class
"""


def inherits_from(obj, a_class):
    """Returns true if element is in  a subclass of  a_class
    but not on a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
