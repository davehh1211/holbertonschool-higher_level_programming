#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”

    Args:
        filename ([type]): [description]

    Returns:
        [json file]: [description]
    """
    with open(filename, mode='r', encoding='UTF8') as myfile:
        return json.load(myfile)
