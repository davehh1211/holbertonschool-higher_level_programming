#!/usr/bin/python3
"-square.py - defines the area of a square"


class Square:
    """
    Class that defines the area a square
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
            
    def area(self):
        "definition of area of the square"
        area = self.__size * self.__size
        return area
