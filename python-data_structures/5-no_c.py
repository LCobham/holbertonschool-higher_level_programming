#!/usr/bin/env python3


def no_c(my_string):
    while my_string.find('c') >= 0:
        x = my_string.find('c')
        my_string = my_string[: x] + my_string[x + 1:]
    while my_string.find('C') >= 0:
        x = my_string.find('C')
        my_string = my_string[:x] + my_string[x + 1:]
    return my_string
