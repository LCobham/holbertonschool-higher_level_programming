#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_del = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys_to_del.append(i)
    for key in keys_to_del:
        del a_dictionary[key]
    return a_dictionary
