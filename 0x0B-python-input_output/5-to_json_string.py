#!/usr/bin/python3
"""This module contains a function called to_json_string"""


import json


def to_json_string(my_obj):
    """to_json_string function that transform  python my_obj to json string

    Args:
        my_obj (objetc): python object
    """
    return(json.dumps(my_obj))
