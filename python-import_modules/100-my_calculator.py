#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    if argc != 4:
        sys.exit("Usage: ./100-my_calculator.py <a> <operator> <b>")

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ['+', '-', '*', '/']

    if operators[0] == sys.argv[2]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    elif operators[1] == sys.argv[2]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif operators[2] == sys.argv[2]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    elif operators[3] == sys.argv[2]:
        print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
