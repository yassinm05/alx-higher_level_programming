#!/usr/bin/python3
"""a function that write to a file"""


def append_write(filename="", text=""):
    """a function that appends"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
