#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as i:
        print("Exception: {}".format(i), file=stderr)
        return None
