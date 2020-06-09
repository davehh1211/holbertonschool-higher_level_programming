#!/usr/bin/python3
"""test to evaluate base
"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
import pep8


class TestBase(unittest.TestCase):
    """checks the class"""

    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_baseid(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        baseneg = Base(-4)
        self.assertEqual(baseneg.id, -4)
        baseint = Base(52)
        self.assertEqual(baseint.id, 52)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        strs = 12
        base2 = Base(strs)
        self.assertEqual(base2.id, 12)
        base2 = Base(3.6)
        self.assertEqual(base2.id, 3.6)
        base3 = Base('hello')
        self.assertEqual(base3.id, 'hello')
        basebool = Base(True)
        self.assertEqual(basebool.id, True)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

        empty_dictionary = Base.to_json_string([])
        self.assertIsInstance(empty_dictionary, str)
        self.assertEqual(empty_dictionary, '[]')

        none_dic = Base.to_json_string(None)
        self.assertIsInstance(none_dic, str)
        self.assertEqual(none_dic, '[]')

        list_test = Base.from_json_string(json_dictionary)
        self.assertIsInstance(list_test, list)
        self.assertEqual(list_test[0]['width'], dictionary['width'])
        self.assertEqual(list_test[0]['height'], dictionary['height'])
        self.assertEqual(list_test[0]['x'], dictionary['x'])
        self.assertEqual(list_test[0]['y'], dictionary['y'])
        self.assertEqual(list_test[0]['id'], dictionary['id'])

    """def test_base_error(self):"""

    def test_save_to_file(self):
        l1 = Rectangle(15, 20, 30, 40)
        l2 = Rectangle(25, 8)
        Rectangle.save_to_file([l1, l2])
        with open("Rectangle.json", "r") as myfile:
            self.assertEqual(json.loads(myfile.read()), [{"y": 40, "x": 30, "width": 15,
                                                          "height": 20, "id": 3},
                                                         {"y": 0, "x": 0, "width": 25,
                                                          "height": 8, "id": 4}])
            os.remove("Rectangle.json")

    # def test_from_json_string(sef):

        # def test_create(self):

        # def test_load_from_file(self):
