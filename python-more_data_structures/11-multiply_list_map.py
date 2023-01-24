#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    cpy = my_list.copy()
    num_list = [number for i in range(len(cpy))]
    return list(map(lambda x, y: x * y, cpy, num_list))
