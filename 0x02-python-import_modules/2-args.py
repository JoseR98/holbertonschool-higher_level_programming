#!/usr/bin/python3
from sys import argv
len_args = len(argv) - 1
if __name__ == "__main__":
    print("{:d} {}{}".format(len_args, "argument\
" if len_args == 1 else "arguments", ".\
" if len_args == 0 else ":"))
    i = 1
    while i <= len_args:
        print("{:d}: {}".format(i, argv[i]))
        i += 1
