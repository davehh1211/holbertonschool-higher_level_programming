#!/usr/bin/python3
"""say my name function
"""


def say_my_name(first_name, last_name=""):
    """function that prints a name.

    Arguments:
        first_name {[str]} -- the first name of the user.

    Keyword Arguments:
        last_name {str} -- the last name of the user (default: {""})

    Raises:
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name is None:
        raise
    print("My name is {} {}".format(first_name, last_name))
