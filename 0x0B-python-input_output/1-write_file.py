#!/usr/bin/python3
"""module for opening file"""


def write_file(filename="", text=""):
    """write and count a string to a file"""
    with open(filename, "w", encoding='utf-8') as file1:
        return file1.write(text)
