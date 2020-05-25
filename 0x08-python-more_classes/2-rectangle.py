#!/usr/bin/python3
"""defines a rectangle
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

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that finds the area of a rectangle.

        Returns:
            int -- the result of the multiplication
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Method that finds the perimeter of a rectangle.

        Returns:
            [int] -- the addition of the sides of the rectangle
            if either width or height is 0, returns 0.
        """
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        perimeter = (self.__width + self.__height) * 2
        return perimeter
