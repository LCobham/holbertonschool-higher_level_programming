#!/usr/bin/python3
"""
    This module defines a function to check is an object is an instance
    of a given class, or belongs to a subclass of the given class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if element is in a subclass of a_class"""
    return issubclass(type(obj), a_class)
