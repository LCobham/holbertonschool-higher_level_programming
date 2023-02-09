#!/usr/bin/python3
"""
    This module defines a function that tries to
    add an attribute to a class
"""


def add_attribute(obj, name, value):
    """Add attribute to a given object"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
