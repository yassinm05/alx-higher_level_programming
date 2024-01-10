#!/usr/bin/python3
"""module for opening file"""


def read_file(filename=""):
    """opens a file"""
    with open(filename, encoding='utf-8') as file1:
        print(file1.read(), end="")
