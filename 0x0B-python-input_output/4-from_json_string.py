#!/usr/bin/python3
"""a function that returns the obj"""

import json


def from_json_string(my_str):
    """return a json str"""
    return json.loads(my_str)
