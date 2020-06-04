#!/usr/bin/python3
"""Write a class Student that defines a student by
"""


class Student:
    """Write a class Student that defines a student by
    """

    def __init__(self, first_name, last_name, age):
        """Write a class Student that defines a student by

        Args:
            first_name ([str]): [description]
            last_name ([str]): [description]
            age ([int]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
