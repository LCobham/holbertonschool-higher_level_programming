#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""

import unittest
import sys
import io
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareClass(unittest.TestCase):
    """Simple class to test behaviour of Square objects"""

    def setUp(self):
        self.s1 = Square(5, id=101)
        self.s2 = Square(2, id=102)
        self.s3 = Square(1, 2, 3, 10)

    # Test correct inheritance from Sqaure class
    def testInheritance(self):
        self.assertTrue(type(self.s1) is Square)
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIsInstance(self.s1, Base)
        self.assertTrue(issubclass(type(self.s1), Rectangle))
        self.assertTrue(issubclass(type(self.s1), Base))

    # Test size is set correctly
    def testSize(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 2)
        self.s1.size = 3
        self.assertEqual(self.s1.size, 3)

    # Test exceptions
    def testSizeExceptions(self):
        with self.assertRaises(TypeError) as cm:
            self.s10 = Square([1, 2, 3], id=-1)
            self.s10.size = "9"
            self.assertEqual("width must be an integer", cm.exception)

        with self.assertRaises(ValueError) as cm:
            self.s10 = Square(0, id=-1)
            self.s10.size = -10
            self.assertEqual("width must be > 0", cm.exception)

    # Test __str__ method
    def testStr(self):
        self.assertEqual(str(self.s1), "[Square] (101) 0/0 - 5")
        self.assertEqual(str(self.s3), "[Square] (10) 2/3 - 1")

    # Test area method of square (inherited from Rectangle)
    def testArea(self):
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 1)

    def testUpdateArgs(self):
        self.assertEqual(str(self.s1), "[Square] (101) 0/0 - 5")
        self.s1.update(102)
        self.assertEqual(str(self.s1), "[Square] (102) 0/0 - 5")
        self.s1.update(102, 3)
        self.assertEqual(str(self.s1), "[Square] (102) 0/0 - 3")
        self.s1.update(102, 3, 4)
        self.assertEqual(str(self.s1), "[Square] (102) 4/0 - 3")
        self.s1.update(102, 3, 4, 5)
        self.assertEqual(str(self.s1), "[Square] (102) 4/5 - 3")

    def testUpdateKwargs(self):
        self.assertEqual(str(self.s1), "[Square] (101) 0/0 - 5")
        self.s1.update(x=4)
        self.assertEqual(str(self.s1), "[Square] (101) 4/0 - 5")
        self.s1.update(id=25, y=6)
        self.assertEqual(str(self.s1), "[Square] (25) 4/6 - 5")
        self.s1.update(id=100, size=2, y=1, x=3)
        self.assertEqual(str(self.s1), "[Square] (100) 3/1 - 2")
        self.s1.update(105, 2, x=10)
        self.assertEqual(str(self.s1), "[Square] (105) 3/1 - 2")

    def testSquareToDictionary(self):
        for square in [self.s1, self.s2, self.s3]:
            square_dic = square.to_dictionary()
            for key, value in square_dic.items():
                self.assertEqual(getattr(square, key), value)


if __name__ == '__main__':
    unittest.main()
