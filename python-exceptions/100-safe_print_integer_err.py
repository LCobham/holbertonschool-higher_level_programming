#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        err_string = "Exception: {}\n".format(err)
        sys.stderr.write(err_string)
        return False
    except TypeError as err:
        err_string = "Exception: {}\n".format(err)
        sys.stderr.write(err_string)
        return False
