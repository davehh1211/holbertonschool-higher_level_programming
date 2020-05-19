#!/usr/bin/python3
"2-square.py - defines a square with a private attribute and exceptions"


class Square:
    """
    Class that defines a squared
    If the size is not an integer raises a Type Error
    If the size is less than zero raises a Value error
    Args:
        Size (int): Private, Size of the square
    """
    def __init__(self, size=0):
        "Initialization of instance with size"
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
