#!/usr/bin/python3
"""This module contains a function called write_file"""


def write_file(filename="", text=""):
    """write_file function that overwrite a file or create new file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): string to write inside the file. Defaults to "".
    """
    try:
        with open("{}".format(filename), "w", encoding="utf-8") as a_file:
            num_chars = a_file.write(text)
            return num_chars
    except:
        raise Exception
