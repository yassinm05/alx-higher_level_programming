#!/usr/bin/python3
"""a module for is_same_class method"""


def is_same_class(obj, a_class):
    """true if the object is exactly an instance of the specified class"""
    return type(obj) == a_class
