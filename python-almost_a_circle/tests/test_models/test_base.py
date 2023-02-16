#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseId(unittest.TestCase):
    """Simple class for testing Base class"""
    def testBaseIdWithArg(self):
        self.b98 = Base(98)
        self.b49 = Base(id=49)
        self.b101 = Base(101)
        self.r1 = Rectangle(1, 2, id=7)
        self.s1 = Square(5, id=10)
        self.assertEqual(self.b98.id, 98)
        self.assertEqual(self.b49.id, 49)
        self.assertEqual(self.b101.id, 101)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.s1.id, 10)

    def testBaseIdNoArg(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b11 = Base(11)
        self.b12 = Base(12)
        self.b4 = Base()
        self.r1 = Rectangle(1, 2)
        self.b14 = Base(18)
        self.s1 = Square(5)
        self.b5 = Base()
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b11.id, 11)
        self.assertEqual(self.b12.id, 12)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.b14.id, 18)
        self.assertEqual(self.s1.id, 6)
        self.assertEqual(self.b5.id, 7)

    def testBaseWithNegOrZero(self):
        self.b0 = Base(0)
        self.neg7 = Base(-7)
        self.neg30 = Base(-30)
        self.assertEqual(self.b0.id, 0)
        self.assertEqual(self.neg7.id, -7)
        self.assertEqual(self.neg30.id, -30)

    def testBaseTupleUnpacking(self):
        self.b9, self.b10 = Base(9), Base(10)
        self.assertEqual(self.b9.id, 9)
        self.assertEqual(self.b10.id, 10)


if __name__ == '__main__':
    unittest.main()
