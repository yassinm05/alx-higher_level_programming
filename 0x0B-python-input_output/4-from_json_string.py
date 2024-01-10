#!/usr/bin/python3
"""module for opening file"""

import json


def from_json_string(my_str):
    """return the json str"""
    return json.loads(my_str)
