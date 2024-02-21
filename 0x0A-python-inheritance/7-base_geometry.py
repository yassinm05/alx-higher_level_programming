#!/usr/bin/python3
"""a module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """a function the calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function for validation"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
