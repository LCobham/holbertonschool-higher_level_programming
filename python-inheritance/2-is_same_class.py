#!/usr/bin/python3
"""
    This module defines a function to check if an object is exactly an
    an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is of type a_class"""
    return type(obj) is a_class
