#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_mylist = len(my_list)
    if idx < 0:
        return my_list
    elif idx > len_mylist - 1:
        return my_list
    my_list[idx] = element
    return my_list
