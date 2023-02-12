#!/usr/bin/python3
"""
    This module defines a function that loads an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Load an object from a JSON file and return it"""
    with open(filename, encoding='utf-8') as f:
        my_obj = json.load(f)

    return my_obj
