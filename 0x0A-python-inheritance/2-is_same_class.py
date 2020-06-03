#!/usr/bin/python3
"""Write a function that returns True
    if the object is exactly an instance
    of the specified class ; otherwise False.
    """


def is_same_class(obj, a_class):
    """function that return instance of an object

    Arguments:
        obj {[any]} -- object to be evaluated
        a_class {[class]} -- class to be compared

    Returns:
        True or false.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
