#!/usr/bin/python3
"""a module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class that is a sub from rectangle"""
    def __init__(self, size):
        """construct"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ a method that calculate the area"""
        return self.__size * self.__size

    def __str__(self):
        """ string fun that is discription"""
        return "[square] " + str(self.__size) + "/" + str(self.__size)
