#!/usr/bin/python3
"""module for opening file"""

import json


def save_to_json_file(my_obj, filename):
    """write a json file to a file"""
    with open(filename, "w", encoding='utf-8') as file1:
        json.dump(my_obj, file1)
