#!/usr/bin/python3
"""class and json"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """init the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the student to json"""
        return self.__dict__
