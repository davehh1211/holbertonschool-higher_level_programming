#!/usr/bin/python3
"""test to check the method"""

import unittest
import pep8
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_isintwidth(self):
        list1 = Square(10)
        self.assertEqual(list1.id, 1)
        list2 = Square(10, 2, 1)
        self.assertEqual(list2.id, 2)
        list3 = Square(5, 10, 6, 8)
        self.assertEqual(list3.id, 8)

    def test_area(self):
        list4 = Square(5, 8)
        self.assertEqual(list4.area(), 25)
        list4 = Square(10)
        self.assertEqual(list4.area(), 100)
        list4 = Square(4, 0, 0, 5)
        self.assertEqual(list4.area(), 16)

    def test_display(self):
        srt1 = "###\n###\n###\n"
        r5 = Square(3)
        tmp = StringIO()
        sys.stdout = tmp
        r5.display()
        self.assertEqual(tmp.getvalue(), srt1)
        tmp.close()
        srt2 = "  ##\n  ##\n"
        r6 = Square(2, 2)
        tmp = StringIO()
        sys.stdout = tmp
        r6.display()
        self.assertEqual(tmp.getvalue(), srt2)
        tmp.close()

    def test_str(self):
        result = Square(5, 1, 3)
        self.assertEqual(result.__str__(), "[Square] (1) 1/3 - 5")
        result = Square(5, 6, 0, 0)
        self.assertEqual(result.__str__(), "[Square] (0) 6/0 - 5")
        result = Square(5, 6)
        self.assertEqual(result.__str__(), "[Square] (2) 6/0 - 5")

    def test_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 10")
        r1.update(89, 25, 15, 5)
        self.assertEqual(r1.__str__(), "[Square] (89) 15/5 - 25")

    def test_to_dict(self):
        r1 = Square(10, 2, 5, 9)
        r1.to_dictionary()
        self.assertEqual(r1.__str__(), "[Square] (9) 2/5 - 10")
        r1 = Square(11, 6, 8, 4)
        r1.to_dictionary()
        self.assertEqual(r1.__str__(), "[Square] (4) 6/8 - 11")

    def test_error_rectanglevalue(self):
        self.assertRaises(ValueError, Square, 2, -1, 6, 8)
        self.assertRaises(ValueError, Square, -2, 5, 5)
        self.assertRaises(ValueError, Square, 2, 5, -5, 4)
        self.assertRaises(ValueError, Square, 0, 5, 5)

    def test_error_rectangletype(self):
        self.assertRaises(TypeError, Square, 2, 5, 5, 3, 8, 6)
        self.assertRaises(TypeError, Square, (2, 5), 5)
        self.assertRaises(TypeError, Square, "hello", 5)
        self.assertRaises(TypeError, Square, [4, 5, 6])
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, True, False, False)
        self.assertRaises(TypeError, Square, False)
