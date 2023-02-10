#!/usr/bin/python3
"""
    This module defines a function that reads and prints the
    contents of a file.
"""


def read_file(filename=""):
    """Reads and prints the contents of a file.
    Encoding is assumed to be utf-8.
    """
    with open(filename, encoding='utf-8') as f:
        myFile = f.read()

    print(myFile)
