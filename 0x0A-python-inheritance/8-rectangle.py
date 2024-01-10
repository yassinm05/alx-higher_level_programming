#!/usr/bin/python3
"""module for empty class"""


class Rectangle(BaseGeometry):

    """a subclass"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        slef.integer_validator("height", height)
        self.__width = width
        self.__height = height
