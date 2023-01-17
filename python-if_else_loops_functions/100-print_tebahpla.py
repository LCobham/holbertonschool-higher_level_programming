#!/usr/bin/python3

for i in range(123, 96, -1):
    if i % 2 == 0:
        c = chr(i)
    else:
        c = chr(i - 32)
    print("{}".format(c), end='')
