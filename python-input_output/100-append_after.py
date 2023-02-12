#!/usr/bin/python3
"""
    This module defines a function that inserts a line of text
    to a file after each occurrance of a specific string.
"""


import os


def append_after(filename="", search_string="", new_string=""):
    """Append new_string after each occurrance of search_string"""
    with open(filename, 'r', encoding="utf-8") as f:
        with open(filename + '__COPY__', 'w', encoding='utf-8') as rf:
            for line in f:
                rf.write(line)
                if search_string in line:
                    rf.write(new_string)
    os.rename(filename + '__COPY__', filename)
