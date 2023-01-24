#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    num_list = [number] * len(my_list)
    return list(map(lambda x, y: x * y, my_list.copy(), num_list))
