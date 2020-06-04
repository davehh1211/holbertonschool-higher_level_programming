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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance

        Args:
            attrs ([list], optional): [list of attributes of the class].

                Returns:
                        [dict]: [the whole dict]
                """
        newdictionary = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    newdictionary[key] = value
            return newdictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance:

        Args:
            json ([dict,list]): [description]
        """
        if not json:
            return
        self.__dict__ = json
