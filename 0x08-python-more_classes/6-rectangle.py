#!/usr/bin/python3
"""
class to define a rectangle
"""


class Rectangle:
    """class that defines a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialization of attributes
        Keyword Arguments:
            width {int} -- [how long is the rectangle] (default: {0})
            height {int} -- [how tall is the rectangle] (default: {0})
        Raises:
            TypeError: width must be an integer
            ValueError: "width must be >= 0"
            TypeError: "height must be an integer"
            ValueError: height must be >= 0

        Returns:
            [int] -- [the value required]
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """method to print in str.

        Returns:
            [char] -- [print using #]
        """
        var_rect = ""
        if self.__width is 0 or self.__height is 0:
            return var_rect
        for i in range(self.__height - 1):
            var_rect += ("#" * self.__width) + "\n"
        var_rect += ("#" * self.__width)
        return var_rect

    def __repr__(self):
        """method to return

        Returns:
            [type] -- [description]
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
