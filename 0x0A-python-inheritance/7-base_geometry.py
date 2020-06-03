#!/usr/bin/python3
"""Write a class BaseGeometry
(based on 5-base_geometry.py)
Raises:
    Exception: [area() is not implemented]
"""


class BaseGeometry:
    """BaseGeometry
    """

    def area(self):
        """Area in exception

        Raises:
            Exception: [area() is not implemented]
                """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value

        Arguments:
            name {[string]} -- [description]
            value {[int]} -- [description]

        Raises:
            TypeError: [must be an integer]
            ValueError: [dmust be greater than 0]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
