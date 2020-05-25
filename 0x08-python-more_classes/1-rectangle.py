#!/usr/bin/python3
"""this function defines a rectangle area.
"""


class Rectangle:
    """ Class that defines the a rectangle
    """

    def __init__(self, width=0, height=0):
        """Instance to initialize the variables.
        Keyword Arguments:
            width {int} -- [the longitude of the figure] (default: {0})
            height {int} -- [the altitude of the figure] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
