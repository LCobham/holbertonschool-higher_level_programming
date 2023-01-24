#!/usr/bin/python3
def multiply_list_map(my_list=[], n=0):
    return list(map(lambda x, y: x * y, my_list.copy(), [n] * len(my_list)))
