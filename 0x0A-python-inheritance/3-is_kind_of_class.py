#!/usr/bin/python3
"""module for is_kind_of_class fun"""


def is_kind_of_class(obj, a_class):
    """check if  object is an instance of, or if the object is an
    instance of a class that inherited from the specified class"""
    return isinstance(obj, a_class)
