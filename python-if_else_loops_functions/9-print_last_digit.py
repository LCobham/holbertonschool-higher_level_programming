#!/usr/bin/python3

def abs(x):
    return x if x > 0 else -x


def print_last_digit(number):
    digit = abs(number) % 10
    print(digit, end='')
    return (digit)
