#!/usr/bin/python3


def search_replace(my_list, search, replace):
    length = len(my_list)
    srch_l = [search for i in range(length)]
    rplc_l = [replace for i in range(length)]
    res = map(lambda x, y, z: z if x == y else x, my_list, srch_l, rplc_l)
    return list(res)
