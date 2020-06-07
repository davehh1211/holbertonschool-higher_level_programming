#!/usr/bin/python3
"""The goal of it is to manage
id attribute in all your future
classes and to avoid duplicating
the same code (by extension, same bugs)
"""


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
