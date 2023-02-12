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

    def to_json(self, attrs=None):
        """Return the dict representation of the object
        to serialize into JSON file
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__

        if not all(type(attrs[i]) is str for i in range(len(attrs))):
            return self.__dict

        my_dict = dict()
        for at in attrs:
            if at in self.__dict__.keys():
                my_dict[at] = self.__dict__[at]
        return my_dict

    def reload_from_json(self, json):
        """replace all attributes of the Student instance"""
        for key in json:
            setattr(self, key, json[key])
