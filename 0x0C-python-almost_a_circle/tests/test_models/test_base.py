#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

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

    """def test_base_error(self):"""

    # def test_to_json_string(self):

    # def test_save_to_file(self):

    # def test_from_json_string(sef):

    # def test_create(self):

    # def test_load_from_file(self):

    # def
