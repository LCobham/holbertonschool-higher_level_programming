#!/usr/bin/python3
"""
    This module defines the Student class
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dict representation of the object
        to serialize into JSON file
        """
        return self.__dict__
