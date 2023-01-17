#!/usr/bin/python3

import sys

if __name__ == '__main__':
    arguments = len(sys.argv)
    if arguments > 1:
        if arguments > 2:
            print("{} arguments:".format(arguments - 1))
        else:
            print("{} argument:".format(arguments - 1))

        for i in range(1, arguments):
            print("{}: {}".format(i, sys.argv[i]))

    else:
        print("0 arguments.")
