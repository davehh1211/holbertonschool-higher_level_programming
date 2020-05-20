#!/usr/bin/python3
"5-square.py - defines a square in different instances"


class Square:
    """
    Class that defines a square in different instances
    If the size is not an integer raises a Type Error
    If the size is less than zero raises a Value error
    Args:
        Size (int): Private, Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        "definition of area of the square"
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        "protecting the data"
        return self.__size

    @size.setter
    def size(self, value):
        "protecting from getting a wrong data"
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        "protecting the var"
        return self.position

    @position.setter
    def position(self, value):
        "proteting the data from wrong values"
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = value

    def my_print(self):
        "printing hashtags as a square"
        if self.__size is 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            if (self.__position[0] > 0):
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
