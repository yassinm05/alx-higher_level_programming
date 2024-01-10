#!/usr/bin/python3
"""module for empty class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """a subclass"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        """representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
