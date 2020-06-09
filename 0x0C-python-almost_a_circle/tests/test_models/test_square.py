#!/usr/bin/python3
"""test to check the method"""

import unittest
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_isintwidth(self):
        list1 = Square(10)
        self.assertEqual(list1.id, 1)
        list2 = Square(10, 2, 1)
        self.assertEqual(list2.id, 2)
        list3 = Square(5, 10, 6, 8)
        self.assertEqual(list3.id, 8)

    """def test_attributes(self):

    def test_update(self):

    def test_to_dictionary(self):

    def test__str__(self):"""
