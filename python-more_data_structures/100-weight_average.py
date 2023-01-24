#!/usr/bin/python3


def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0

    total = list(map(lambda x: x[0] * x[1], my_list))
    divisor = list(map(lambda y: y[1], my_list))

    return sum(total)/sum(divisor)
