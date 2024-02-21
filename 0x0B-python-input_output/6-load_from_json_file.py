#!/usr/bin/python3
"""a function that use json"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
