#!/usr/bin/python3
"""a method for inherits_from module"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    flag = isinstance(obj, a_class) and type(obj) != a_class
    return flag
