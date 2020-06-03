#!/usr/bin/python3
""" class that inherits from rectangle

Returns:
    printing format.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that inherits rectangle

    Arguments:
        Rectangle {[int]} -- the size
    """

    def __init__(self, size):
        """isntance of value validator
        Arguments:
            size {[int]} -- the area of the rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
