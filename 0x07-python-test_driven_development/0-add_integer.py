#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Adds two ints

    Raises:
      TypeError : if a, b are not inegers

    Returns:
      the sum of the ints
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
