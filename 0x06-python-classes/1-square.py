#!/usr/bin/python3
"1-square.py - defines a square with a private attribute"


class Square:
    """
    Class that defines a square
    Args:
        Size (int): Private, Size of the square
    """
    def __init__(self, size):
        "Initialization of instance with size"
        self.__size = size
