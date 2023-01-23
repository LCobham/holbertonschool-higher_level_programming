#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None

    cpy = my_list.copy()
    cpy.sort()
    return cpy[length - 1]
