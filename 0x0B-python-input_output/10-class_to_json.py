#!/usr/bin/python3
"""Write a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """function that returns the dictionary
    description with simple data structure

    Args:
        obj ([object of a class]): [description]

    Returns:
        [type]: [description]
    """
    return obj.__dict__
