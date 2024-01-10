#!/usr/bin/python3
"""module for opening file"""

import json


def load_from_json_file(filename):
    """load from file"""
    with open(filename, "r", encoding='utf-8') as file1:
        return json.load(file1)
