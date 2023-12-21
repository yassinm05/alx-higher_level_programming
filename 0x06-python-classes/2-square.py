#!/usr/bin/python3
"""sqaure module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """constructor
        args:
            size: length of the side
        raises:
            TypeError: if size is not an int
            ValueError:if size is less than 0
        """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
