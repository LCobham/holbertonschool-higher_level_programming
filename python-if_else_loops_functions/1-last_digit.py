#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 if number > 0 else -(abs(number) % 10)
print(f"Last digit of {number} is ", end='')
if digit == 0:
    print(f"{digit} and is 0")
elif digit > 5:
    print(f"{digit} and is greater than 5")
else:
    print(f"{digit} and is less than 6 and not 0")
