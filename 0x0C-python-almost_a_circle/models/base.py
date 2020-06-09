#!/usr/bin/python3
"""The goal of it is to manage
id attribute in all your future
classes and to avoid duplicating
the same code (by extension, same bugs)
"""
import json
import csv


class Base:
    """base class for the rest of the projects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            "the code below,everytime an object is created\
            the class calls its attribute and increment one\
            only if fullfill the condition"
            Base.__nb_objects += 1
            "then, assign the increment to the var id"
            self.id = Base.__nb_objects
        else:
            "it an argument is given, it passes normally"
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

                Args:
                        list_dictionaries ([type]): [description]

                Returns:
                        [type]: [description]
                """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

                Args:
                        list_objs ([type]): [description]
                """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='UTF8') as myfile:
            if list_objs is None:
                json.dumps("[]", myfile)
            else:
                list_own = []
                for obj_lists in list_objs:
                    tmp_dictio = cls.to_dictionary(obj_lists)
                    list_own.append(tmp_dictio)
            json_list_dict = cls.to_json_string(list_own)
            myfile.write(json_list_dict)

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """[summary]

                Returns:
                        [type]: [description]
                """
        filename = "{}.json".format(cls.__name__)
        if not filename:
            return "[]"
        else:
            with open(filename, mode='r', encoding='UTF8') as myfile:
                list_inst = myfile.read()
                str_js = cls.from_json_string(list_inst)
                l_js = []
                for instan_el in str_js:
                    aux = cls.create(**instan_el)
                    l_js.append(aux)
                return l_js
