#!/usr/bin/python3
"""Function to add two integers
    """


def add_integer(a, b=98):
    """Function to add two integers

    Arguments:
        a {int} -- Integer to be added

    Keyword Arguments:
        b {int} -- Integer to be added (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int -- result of the addition of two.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('Nan') or type(b) is float('NaN'):
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
