#!/usr/bin/python3
"""a function the reads a file"""


def read_file(filename=""):
    """reads the file """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
