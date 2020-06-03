#!/usr/bin/python3
"""This module contain a function called append_write"""


def append_write(filename="", text=""):
    """append_write function that

    [extended_summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open("{}".format(filename), "a", encoding="utf-8") as a_file:
        num_char_add = a_file.write(text)
        return num_char_add
