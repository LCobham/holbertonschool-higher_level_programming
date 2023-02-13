#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
import sys

sys.path.append('/root/holbertonschool-higher_level_programming/python-almost_a_circle/')
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Simple class for testing Rectangle class attributes and functionality"""

    # Needs fixing... when run multiple times, ID's change into unexpected values #
    # --------------------------------------------------------------------------- #
    def setUp(self):
        self.r1 = Rectangle(2, 3)
        self.r2 = Rectangle(4, 4)
        self.r3 = Rectangle(1, 5, id=101)
        self.r4 = Rectangle(2, 2, 0, 0, 8)

    # Test the ID of different instances of Rectangle
    def testRectangleId(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 101)
        self.assertEqual(self.r4.id, 8)

    # Test if width value is set correctly. Test exceptions on setter.
    # Check if attribute is private
    def testRectangleWidth(self):
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 1)

        self.r3.width = 4
        self.assertEqual(self.r3.width, 4)
        self.r3.width = 1
        self.assertEqual(self.r3.width, 1)

        with self.assertRaises(TypeError):
            self.r1.width = "Hello"
            self.r2.width = ["a", "list"]
            self.r3.width = {"a": "dict", (1, 2): "wee"}
            self.r4.width = 2.7
        
        with self.assertRaises(ValueError):
            self.r1.width = 0
            self.r2.width = -5
        
        self.assertTrue('_Rectangle__width' in self.r1.__dict__)

    # Test if height value is set correctly. Test exceptions on setter.
    # Check if attribute is private
    def testRectangleHeight(self):
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r2.height, 4)

        self.r3.height = 2
        self.assertEqual(self.r3.height, 2)
        self.r3.height = 5
        self.assertEqual(self.r3.height, 5)

        with self.assertRaises(TypeError):
            self.r1.height = "Hello"
            self.r2.height = ["a", "list"]
            self.r3.height = {"a": "dict", (1, 2): "wee"}
            self.r4.height = 2.7
        
        with self.assertRaises(ValueError):
            self.r1.height = 0
            self.r2.height = -5


if __name__ == '__main__':
    unittest.main()