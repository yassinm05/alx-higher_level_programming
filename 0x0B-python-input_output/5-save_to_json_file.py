#!/usr/bin/python3
"""a function that use json"""


import json


def save_to_json_file(my_obj, filename):
    """write the json to a file"""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
