#!/usr/bin/python3
"""Write a function that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    """Function to get the inheritance of an object

    Arguments:
        obj {[to be checked]} -- object to be evaluated

        Returns:
                True or false
        """
    return dir(obj)
