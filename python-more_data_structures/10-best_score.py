#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    items = list(a_dictionary.items())
    items.sort(key=lambda x: x[1])
    return items[-1][0]
