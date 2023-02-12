#!/usr/bin/python3
"""
    This module defines a function that inserts a line of text
    to a file after each occurrance of a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string after each occurrance of search_string"""
    with open(filename, 'r+', encoding="utf-8") as f:
        new_contents = ''
        for line in f:
            new_contents += line
            if search_string in line:
                new_contents += new_string
        f.seek(0)
        f.write(new_contents)
