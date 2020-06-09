#!/usr/bin/python3
"""Write the class Square that
inherits from Rectangle:
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Write the class Square that
    inherits from Rectangle:

    Args:
        Rectangle ([class]): [inherits from rectangle class]
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.__width = size
        self.__height = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>)
        <x>/<y> - <size> - in our case, width or height
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public
        method def update(self, *args, **kwargs)
        that assigns attributes:
        """
        if args is not None:
            try:
                self.id = args[0]
                self.__size = args[1]
                self.__size = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except (IndexError):
                pass
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Update the class Square by adding
        the public method def to_dictionary(self):
        that returns the dictionary representation of a Square:

        Returns:
            [list]: [dictionary updated]
        """
        dicto = {'id': self.id, 'size': self.size,
                 'x': self.x,
                 'y': self.y}
        return dicto
