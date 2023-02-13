#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
import sys

sys.path.append('/root/holbertonschool-higher_level_programming/python-almost_a_circle/')
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Simple class for testing Base class"""
    def setUp(self):
        self.b1 = Base()
        self.b98 = Base(98)
        self.b79 = Base(id=79)
        self.b2 = Base()
        self.b3, self.b4 = Base(), Base()
        self.b5 = Base(-7)
        self.b0 = Base(0)

    def testBaseId(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b98.id, 98)
        self.assertEqual(self.b79.id, 79)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual((self.b3.id, self.b4.id), (3, 4))
        self.assertEqual(self.b5.id, -7)
        self.assertEqual(self.b0.id, 0)


if __name__ == '__main__':
    unittest.main()