#!/usr/bin/python3
"""a function that write to a file"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
