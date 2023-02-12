#!/usr/bin/python3
"""
    This module appends all command line arguments to an ongoing list
    which is saved in the file add_item.json
    If file doesn't exist, it is created.
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    args = sys.argv[1:]
    try:
        in_file = load_from_json_file("add_item.json")
        final = in_file + args
        save_to_json_file(final, "add_item.json")

    except FileNotFoundError:
        save_to_json_file(args, "add_item.json")


if __name__ == '__main__':
    main()
