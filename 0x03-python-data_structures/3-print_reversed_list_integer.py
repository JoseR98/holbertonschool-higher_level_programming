#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_mylist = len(my_list) - 1
    if len_mylist >= 0:
        while len_mylist >= 0:
            print("{:d}".format(my_list[len_mylist]))
            len_mylist -= 1
