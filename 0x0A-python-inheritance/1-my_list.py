#!/usr/bin/python3
"""this is the module of the class mylist"""


class MyList(list):
    """the class of mylist"""
    def print_sorted(self):
        """function thta return the list sorted"""
        print(sorted(self))
