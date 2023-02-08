#!/usr/bin/python3
"""
    This module defines a class that inherits from the
    list class.
"""


class MyList(list):
    """New list class with additional functionality"""

    def print_sorted(self):
        """Prints the list in sorted order and return new list"""
        return sorted(self)
