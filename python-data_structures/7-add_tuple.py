#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        return add_tuple(tuple(list(tuple_a) + [0]), tuple_b)
    if len(tuple_b) < 2:
        return add_tuple(tuple_a, tuple(list(tuple_b) + [0]))
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
