#!/usr/bin/python3

import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    res = 0

    for i in range(1, argc):
        res = res + int(sys.argv[i])
    print("{}".format(res))
