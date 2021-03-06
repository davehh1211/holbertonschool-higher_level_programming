#!/usr/bin/python3
"comment David"
import math


class MagicClass:
    "comment"

    def __init__(self, radius=0):
        "comment David"
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        "comment"
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        "comment"
        return 2 * math.pi * self._MagicClass__radius
