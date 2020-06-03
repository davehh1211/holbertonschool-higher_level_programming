#!/usr/bin/python3
"""Write a function that writes
an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes
    an Object to a text file

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, mode='w', encoding='UTF8') as myfile:
        return json.dump(my_obj, myfile)
