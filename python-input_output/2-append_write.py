#!/usr/bin/python3
"""
    This module defines a function to append to a file.
"""


def append_write(filename="", text=""):
    """Append a text to a file. Return the n of chars written"""
    with open(filename, 'a', encoding='utf-8') as f:
        nChars = f.write(text)

    return nChars
