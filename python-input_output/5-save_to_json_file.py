#!/usr/bin/python3
"""
    This module defines a function to write and obj to a file
    using the JSON representation of that object.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes a file with the JSON representation of an object"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
