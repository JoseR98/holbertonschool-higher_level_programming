#!/usr/bin/python3
"""This module contains a function called def class_to_json"""


import json


def class_to_json(obj):
    """class_to_json function that return dict representation in json format

    Args:
        obj (class): is a class
    """
    return json.dumps(obj.__dict__)
