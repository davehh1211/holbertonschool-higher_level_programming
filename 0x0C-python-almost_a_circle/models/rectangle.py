#!/usr/bin/python3
"""Write the class
Rectangle that inherits from Base:
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base

    Args:
        Private instance attributes,
        each with its own public getter and setter
        Base ([class]): []
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [private]
            height ([type]): [prviate]
            x (int, optional): [private]. Defaults to 0.
            y (int, optional): [private]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        "Call the super class with id -\
        this super call with use the logic\
        of the __init__ of the Base class"
        self.width = width
        "to correct likely"
        self.height = height
        self.x = x
        self.y = y

    """Why private attributes with getter/setter?
    Why not directly public attribute?
    Because we want to protect attributes of our class.
    With a setter, you are able to validate what a
    developer is trying to assign to a variable.
    So after, in your class you can “trust” these attributes.
    """
    @property
    def width(self):
        """getter width

        Returns:
                [width]: [private attribute]
        """
        return self.__width

    @width.setter
    def width(self, valwid):
        """setter width

        Args:
            valwid ([private value]): [description]

        Raises:
            TypeError: [if object is not an integer]
            ValueError: [if value is less than 0]
        """
        if type(valwid) is not int:
            raise TypeError("width must be an integer")
        if valwid <= 0:
            raise ValueError("width must be > 0")
        self.__width = valwid

    @property
    def height(self):
        """getter height
        """
        return self.__height

    @height.setter
    def height(self, heightt):
        """setter hiehgt

        Args:
            heightt ([private vlaue]): [private]

        Raises:
            TypeError: [if value is not int]
            ValueError: [if value is less than 0]
        """
        if type(heightt) is not int:
            raise TypeError("height must be an integer")
        if heightt <= 0:
            raise ValueError("height must be > 0")
        self.__height = heightt

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, xe):
        if type(xe) is not int:
            raise TypeError("x must be an integer")
        if xe < 0:
            raise ValueError("x must be >= 0")
        self.__x = xe

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, ye):
        if type(ye) is not int:
            raise TypeError("y must be an integer")
        if ye < 0:
            raise ValueError("y must be >= 0")
        self.__y = ye

    def area(self):
        """returns the area value of the Rectangle

                Returns:
                        [int]: [area]
                """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #
        """
        for lati in range(self.__y):
            print("")
        for i in range(0, self.__height):
            # for j in range(0, (self.__x)):
            print((" " * self.__x) + ('#' * self.__width))

    def __str__(self):
        """returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x,
                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding
        the public method def update(self, *args):
        that assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        This type of argument is called a “no-keyword argument”
        - Argument order is super important.
        """
        if args is not None:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except (IndexError):
                pass
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary
        representation of a Rectangle:
        """
        dicto = {'id': self.id,
                 'width': self.width,
                 'height': self.height,
                 'x': self.x,
                 'y': self.y}
        return dicto
