#!/usr/bin/python3
""" a module for is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """checks is the objects is an instance of,
    or if the object is an instance of a class that inherited from
    """
    return isinstance(obj, a_class)
