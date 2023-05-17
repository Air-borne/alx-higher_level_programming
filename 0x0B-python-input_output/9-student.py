#!/usr/bin/python3
"""
This module contains a class Student that defines a student
"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary version of a student"""
        return self.__dict__
