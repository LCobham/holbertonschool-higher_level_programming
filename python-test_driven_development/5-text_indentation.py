#!/usr/bin/python3
"""
    This module defines a function that prints a text with two new lines
    after the characters '.', '?' or ':'.
"""


def text_indentation(text):
    """Prints a text with 2 newlines after special chars: '.', '?', ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newString = text.replace('.', '.\n\n')
    newString = newString.replace('?', '?\n\n')
    newString = newString.replace(':', ':\n\n')
    newString = newString.replace('\n   ', '\n').replace('\n ', '\n')
    print(f"{newString}", end="")
