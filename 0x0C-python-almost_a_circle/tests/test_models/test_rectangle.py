#!/usr/bin/python3
"""test to check rectangle class
"""

import unittest
import pep8
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_isintwidth(self):
        list1 = Rectangle(10, 5)
        self.assertEqual(list1.id, 1)
        list2 = Rectangle(10, 2, 1)
        self.assertEqual(list2.id, 2)
        list3 = Rectangle(5, 10, 6, 8, 9)
        self.assertEqual(list3.id, 9)
        """if objects are int or different"""

    def test_area(self):
        list4 = Rectangle(5, 8)
        self.assertEqual(list4.area(), 40)
        list4 = Rectangle(5, 10)
        self.assertEqual(list4.area(), 50)
        list4 = Rectangle(4, 6, 0, 0, 5)
        self.assertEqual(list4.area(), 24)

    def test_display(self):
        srt1 = "###\n###\n###\n"
        r5 = Rectangle(3, 3)
        tmp = StringIO()
        sys.stdout = tmp
        r5.display()
        self.assertEqual(tmp.getvalue(), srt1)
        tmp.close()
        srt2 = "\n\n  ##\n  ##\n  ##\n"
        r6 = Rectangle(2, 3, 2, 2)
        tmp = StringIO()
        sys.stdout = tmp
        r6.display()
        self.assertEqual(tmp.getvalue(), srt2)
        tmp.close()

    def test_str(self):
        result = Rectangle(5, 6, 1, 3, 12)
        self.assertEqual(result.__str__(), "[Rectangle] (12) 1/3 - 5/6")
        result = Rectangle(5, 6, 0, 0)
        self.assertEqual(result.__str__(), "[Rectangle] (1) 0/0 - 5/6")
        result = Rectangle(5, 6)
        self.assertEqual(result.__str__(), "[Rectangle] (2) 0/0 - 5/6")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 25, 15, 20, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 20/2 - 25/15")

    def test_error_rectanglevalue(self):
        self.assertRaises(ValueError, Rectangle, 2, -1, 6, 8)
        self.assertRaises(ValueError, Rectangle, -2, 5, 5)
        self.assertRaises(ValueError, Rectangle, 2, 5, -5, 4)
        self.assertRaises(ValueError, Rectangle, 2, 5, 5, -4)
        self.assertRaises(ValueError, Rectangle, 0, 5, 5)
        self.assertRaises(ValueError, Rectangle, 2, 0, 5)

    def test_error_rectangletype(self):
        self.assertRaises(TypeError, Rectangle, 2, 5, 5, 3.6)
        self.assertRaises(TypeError, Rectangle, 2, 5, 5, 3, 8, 6)
        self.assertRaises(TypeError, Rectangle, (2, 5), 5)
        self.assertRaises(TypeError, Rectangle, "hello", 5)
        self.assertRaises(TypeError, Rectangle, [4, 5, 6])
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, True, False, False)
        self.assertRaises(TypeError, Rectangle, False)

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 5, 9)
        r1.to_dictionary()
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 5/9 - 10/2")
        r1 = Rectangle(11, 6, 8, 4, 89)
        r1.to_dictionary()
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 8/4 - 11/6")
