#!/usr/bin/python3
""" """

import json


def load_from_json_file(filename):
    """load_from_json_file [summary]

    Args:
        filename ([type]): [description]
    """
    with open("{}".format(filename), encoding="utf-8") as a_file:
        return json.load(a_file)
