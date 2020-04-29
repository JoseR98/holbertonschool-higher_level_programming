#!/usr/bin/python3
def remove_char_at(str, n):
    copy = list(str)
    i = 0
    while i < len(str):
        if i == n:
            copy[i] = ""
        i += 1
    str_f = listToString(copy)
    return(str_f)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
