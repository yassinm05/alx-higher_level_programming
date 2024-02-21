#!/usr/bin/python3
"""a module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle subclass"""
    def __init__(self, width, height):
        """init function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height