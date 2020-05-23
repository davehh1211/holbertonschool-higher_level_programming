#!/usr/bin/python3
"""Print_square
"""


def print_square(size):
    """function that prints square.

    Arguments:
        size {[int]} -- This is the size of the square

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
        TypeError: [size must be an integer]
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        print("#" * size)
