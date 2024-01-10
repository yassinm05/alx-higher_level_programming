#!/usr/bin/python3
"""module for this fun"""


def add_attribute(obj, attribute, value):
    """a function that adds an attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
