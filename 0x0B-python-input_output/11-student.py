#!/usr/bin/python3
"""class and json"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """init the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dict json"""
        try:
            for attribute in attrs:
                if type(attribute) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        diction = dict()
        for i, j in self.__dict__.items():
            if i in attrs:
                diction[i] = j
        return diction

    def reload_from_json(self, json):
        """reload from json"""
        for i, j in json.items():
            if i in slef.__dict__:
                self.__dict__[i] = value
