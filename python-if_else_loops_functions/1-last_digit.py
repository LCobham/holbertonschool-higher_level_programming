#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit == 0:
    print(f"{digit} and is zero")
elif digit > 5:
    print(f"{digit} and is greater than 5")
else:
    print(f"{digit} and is less than 6 and not 0")
