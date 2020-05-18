#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as i:
        print("Exception: {}".format(i))
        return False
    except TypeError as j:
        print("Exception: {}".format(j))
        return False
