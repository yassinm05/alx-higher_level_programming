#!/usr/bin/python3
"""module for opening file"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, "a", encoding='utf-8') as file1:
        return file1.write(text)
