#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return ret

    except BaseException as err:
        err_message = "Exception: {}\n".format(err)
        sys.stderr.write(err_message)
        return None
