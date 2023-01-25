#!/usr/bin/python3
from dis import dis


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                result = (a ** b) / i
            else:
                raise Exception('Too far')

        except Exception:
            result = b + a
            break

        finally:
            return result
