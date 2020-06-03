#!/usr/bin/python3
"""This module contains a function called save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function

    Args:
        my_obj (object): python object
        filename (str): string name
    """
    with open(filename, "w", encoding="utf-8") as file_a:
        json_file = json.dumps(my_obj)
        file_a.write(json_file)
