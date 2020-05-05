#!/usr/bin/python3
def element_at(my_list, idx):
    len_mylist = len(my_list)
    if idx < 0:
        return None
    elif idx > len_mylist - 1:
        return None
    return (my_list[idx])
