#!/usr/bin/python3
"""
    This module defines a function to write to a file.
"""


def write_file(filename="", text=""):
    """Write a text to a file. Return the n of chars written"""
    with open(filename, 'w', encoding='utf-8') as f:
        nChars = f.write(text)

    return nChars
