#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    for key in cpy:
        cpy[key] = cpy[key] * 2
    return cpy
