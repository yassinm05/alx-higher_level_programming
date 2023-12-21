#!/usr/bin/python3
"""sqaure module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """constructor
        args:
        size: length of the side
        """
        self.__size = size

    @property
    def size(self):
        """getter for size
        raises:
            TypeError: if size is not an int
            ValueError:if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        args:
            value:the value to the size
        raises:
            TypeError: if size is not an int
            ValueError:if size is less than 0
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square
        Returns:
            the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
