#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """checks if he object is an instance of a class that inherited
    (directly or indirectly)from the specified class"""
    return type(obj) != a_class and isinstance(obj, a_class)
