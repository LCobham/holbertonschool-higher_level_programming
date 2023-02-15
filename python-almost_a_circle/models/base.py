#!/usr/bin/python3
"""
    This module creates the Base class
"""


import json


class Base:
    """Base class. Used to set the id of different instances.

    Attributes:
        id: (int) identification number

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the JSON string representation of list_dictionaries
        """
        # If arg is None or is an empty list
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Saves a list of objects (instances which inherit from Base)
            to a JSON file.
        """
        filename = cls.__name__ + '.json'
        dict_list = []

        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        to_dump = Base.to_json_string(dict_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(to_dump)

    @staticmethod
    def from_json_string(json_string):
        """
            Return the python obj from the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Create an object (Rectangle or Square) from a dictionary
            with its attributes and names.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if 'size' in dictionary.keys():
            dummy = Square(1)
            dummy.update(**dictionary)
        else:
            dummy = Rectangle(1, 1)
            dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Return a list of instances, obtained from JSON file.
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_of_dicts = json.load(f)
            print(list_of_dicts)

            return [cls.create(**dic) for dic in list_of_dicts]

        except FileNotFoundError:
            return []
