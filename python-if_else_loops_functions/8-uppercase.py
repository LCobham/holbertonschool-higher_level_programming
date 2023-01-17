#!/usr/bin/python3

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    return False


def uppercase(str):
    for i in str:
        if islower(i):
            c = chr(ord(i) - 32)
        else:
            c = i
        print(c, end='')
    print("")
