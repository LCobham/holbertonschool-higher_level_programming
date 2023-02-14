#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleIdAndInheritance(unittest.TestCase):
    """Simple class for testing Rectangle class id"""

    # Test the ID of different instances of Rectangle
    def testRectangleId(self):
        self.r1 = Rectangle(2, 3, id=1)
        self.r2 = Rectangle(4, 4, id=2)
        self.r3 = Rectangle(1, 5, id=101)
        self.r4 = Rectangle(2, 2, 0, 0, 8)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 101)
        self.assertEqual(self.r4.id, 8)

    def testRectangleInheritance(self):
        self.r5 = Rectangle(1, 1, id=101)
        self.assertTrue(type(self.r5) is Rectangle)
        self.assertFalse(type(self.r5) is Base)
        self.assertTrue(isinstance(self.r5, Base))
        self.assertTrue(issubclass(Rectangle, Base))


class TestRectangleWidth(unittest.TestCase):
    """Simple class to test getter/setter of rectangle width"""
    def setUp(self):
        self.r50 = Rectangle(2, 3, id=50)
        self.r51 = Rectangle(4, 4, id=51)
        self.r52 = Rectangle(1, 5, id=52)
        self.r53 = Rectangle(2, 2, 0, 0, id=8)

    # Test if width value is set correctly.
    def testRectangleWidth(self):
        self.assertEqual(self.r50.width, 2)
        self.assertEqual(self.r51.width, 4)
        self.assertEqual(self.r52.width, 1)

    # Test exception when no width arg is passed
    def testRectangleWidthNoArg(self):
        with self.assertRaises(TypeError) as cm:
            self.r10 = Rectangle(id=101)
            self.assertEqual(
                "__init__() missing 2 required positional arguments:" +
                " 'width' and 'height'",
                cm.exception)
            self.r11 = Rectangle(height=4, id=101)
            self.assertEqual(
                "__init__() missing 1 required positional argument:" +
                " 'width'",
                cm.exception)

    # Test width setter function and correct Exceptions
    def testRectangleWidthSetter(self):
        self.assertEqual(self.r51.width, 4)
        self.r51.width = 3
        self.assertEqual(self.r51.width, 3)
        self.r51.width = 1
        self.assertEqual(self.r51.width, 1)

        with self.assertRaises(TypeError) as cm:
            self.r10 = Rectangle("Hello", 9, id=101)
            self.r11 = Rectangle([3, 2], 6, id=101)
            self.r50.width = {"a": "dict", (1, 2): "wee"}
            self.r50.width = 2.7
            self.assertEqual("width must be an integer", cm.ex)

        with self.assertRaises(ValueError) as cm:
            self.r10 = Rectangle(0, 6, id=101)
            self.r10 = Rectangle(-10, 13, id=101)
            self.r50.width = 0
            self.r50.width = -5
            self.assertEqual("width must be > 0", cm.ex)

    # Test if attribute is private (which indirectly checks getter fun)
    def testWidthPrivateAttr(self):
        self.assertTrue('_Rectangle__width' in self.r50.__dict__)


class TestRectangleHeight(unittest.TestCase):
    """Class to test rectangle height getter / setter and exceptions"""

    def setUp(self):
        self.r50 = Rectangle(2, 3, id=50)
        self.r51 = Rectangle(4, 4, id=51)
        self.r52 = Rectangle(1, 5, id=52)
        self.r53 = Rectangle(2, 2, 0, 0, id=8)

    # Test if height value is set correctly. Test exceptions on setter.
    # Check if attribute is private
    def testRectangleHeight(self):
        self.assertEqual(self.r50.height, 3)
        self.assertEqual(self.r51.height, 4)
        self.assertEqual(self.r52.height, 5)

    # Test exception when no width arg is passed
    def testRectangleHeightNoArg(self):
        with self.assertRaises(TypeError) as cm:
            self.r10 = Rectangle(id=101)
            self.assertEqual(
                "__init__() missing 2 required positional arguments:" +
                " 'width' and 'height'",
                cm.exception)
            self.r11 = Rectangle(width=4, id=101)
            self.assertEqual(
                "__init__() missing 1 required positional argument:" +
                " 'height'",
                cm.exception)

    # Test width setter function and correct Exceptions
    def testRectangleHeightSetter(self):
        self.assertEqual(self.r51.height, 4)
        self.r51.height = 3
        self.assertEqual(self.r51.height, 3)
        self.r51.height = 1
        self.assertEqual(self.r51.height, 1)

        with self.assertRaises(TypeError) as cm:
            self.r10 = Rectangle(7, "A string", id=101)
            self.r11 = Rectangle(2, [3, 2], id=101)
            self.r50.height = {"a": "dict", (1, 2): "wee"}
            self.r50.height = 2.7
            self.assertEqual("height must be an integer", cm.ex)

        with self.assertRaises(ValueError) as cm:
            self.r10 = Rectangle(5, 0, id=101)
            self.r10 = Rectangle(10, -13, id=101)
            self.r50.height = 0
            self.r50.height = -5
            self.assertEqual("height must be > 0", cm.ex)

    # Test if attribute is private (which indirectly checks getter fun)
    def testHeightPrivateAttr(self):
        self.assertTrue('_Rectangle__height' in self.r50.__dict__)


class TestRectangleXY(unittest.TestCase):
    """Simple class to test Rectangle's x and y attr & exceptions"""
    def setUp(self):
        self.r1 = Rectangle(1, 1, id=101)
        self.r2 = Rectangle(2, 3, 4, 5, id=102)
        self.r3 = Rectangle(5, 2, x=1, y=2, id=103)

    def testXattr(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 1)
        self.r1.x = 2
        self.assertEqual(self.r1.x, 2)

    def testYattr(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r3.y, 2)
        self.r1.y = 1
        self.assertEqual(self.r1.y, 1)

    def testExceptions(self):
        with self.assertRaises(ValueError) as cm:
            self.r5 = Rectangle(1, 2, -3, 4, id=101)
            self.assertEqual("x must be >= 0", cm.ex)
            self.r6 = Rectangle(1, 2, 4, -5, id=101)
            self.assertEqual("y must be >= 0", cm.ex)

        with self.assertRaises(TypeError) as cm:
            self.r7 = Rectangle(1, 2, "String", 4, id=101)
            self.r8 = Rectangle(1, 2, [5], 4, id=101)
            self.r9 = Rectangle(1, 2, {"a": "dict"}, 4, id=101)
            self.assertEqual("x must be an integer", cm.ex)

            self.r7 = Rectangle(1, 2, 5, "String", id=101)
            self.r8 = Rectangle(1, 2, 4, [5], id=101)
            self.r9 = Rectangle(1, 2, 3, {"a": "dict"}, id=101)
            self.assertEqual("y must be an integer", cm.ex)


if __name__ == '__main__':
    unittest.main()
