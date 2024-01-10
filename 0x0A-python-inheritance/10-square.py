#!/usr/bin/python3
"""module for empty class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass OF A sub"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area"""
        return self.__size * self.__size
