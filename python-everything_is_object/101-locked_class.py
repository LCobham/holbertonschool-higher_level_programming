#!/usr/bin/python3
"""
    This module creates a 'forzen class', a class for whihc the user can't add
    new attributes.
"""


class LockedClass:
    """Frozen class"""
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
