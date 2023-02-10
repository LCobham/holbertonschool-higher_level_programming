#!/usr/bin/python3
"""
    This module defines a class MyInt that inherits fom int
    but has the == and != methods reversed
"""


class MyInt(int):
    """Functions like int class but
    with == and != methods reversed"""
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
