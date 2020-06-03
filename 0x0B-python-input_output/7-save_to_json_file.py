#!/usr/bin/python3
""" """

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file [summary]

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open('{}'.format(filename),'w',encoding="utf-8") as file_a:
        json_file = json.dumps(my_obj)
        file_a.write(json_file)
