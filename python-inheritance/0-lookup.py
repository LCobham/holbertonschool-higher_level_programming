#!/usr/bin/python3
"""
    This module defines a function to list all available
    atributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of of available attributes and methods of an object"""
    return dir(obj)
