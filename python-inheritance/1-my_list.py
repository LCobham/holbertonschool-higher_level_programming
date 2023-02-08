#!/usr/bin/python3
"""
    This module defines a class that inherits from the
    list class.
"""


class MyList(list):
    """New list class with additional functionality"""

    def print_sorted(self):
        """Rturns the list sorted in ascending order"""
        return sorted(self)
