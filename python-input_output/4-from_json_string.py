#!/usr/bin/python3
"""
    This module defines a function to deserialize a JSON obj
"""


import json


def from_json_string(my_str):
    """Return deserialized str"""
    return json.loads(my_str)
