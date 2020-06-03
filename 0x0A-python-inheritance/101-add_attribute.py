#!/usr/bin/python3
"""set attribute
"""


def add_attribute(object, name, value):
    """ Write a function that adds a new
    attribute to an object if it’s possible

    Arguments:
        object {[object]} -- [description]
        name {[attribute]} -- [description]
        value {[int]} -- [description]

    Raises:
        TypeError: [can't add new attribute]
        """
    if not hasattr(object, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)
