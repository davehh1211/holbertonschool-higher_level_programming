#!/usr/bin/python3
"""Write a function that returns an
object (Python data structure)
represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """[summary]

    Args:
        my_str ([dict]): [dictionary from python]
    """
    return json.loads(my_str)
