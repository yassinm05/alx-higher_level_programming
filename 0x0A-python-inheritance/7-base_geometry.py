#!/usr/bin/python3
"""module for empty class"""


class BaseGeometry:
    """ a basegometry class"""
    def area(self):
        """ that raises an Exception with the message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
