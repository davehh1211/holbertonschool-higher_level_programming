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
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """find the area of the rectangle

        Returns:
            [area] -- [width * height]
                """
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
