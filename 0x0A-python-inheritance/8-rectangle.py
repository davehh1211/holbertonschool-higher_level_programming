#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry

    Arguments:
        BaseGeometry {[class]} -- it has the area and valuevaldiator methods
    """

    def __init__(self, width, height):
        """isntance of value validator
        Arguments:
            width {[int]} -- [longitude]
            height {[int]} -- [altitude]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
