#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Simple class to test Retangle methods"""

    def setUp(self):
        self.r1 = Rectangle(1, 3, id=1)
        self.r2 = Rectangle(5, 4, 1, 2, id=2)
        self.r3 = Rectangle(3, 2, 5, 1, id=3)
        self.r4 = Rectangle(2, 2, id=4)

    # Test area method
    def testArea(self):
        self.assertEqual(self.r1.area(), 3)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 6)
        self.assertEqual(self.r4.area(), 4)

    # Test __str__ method
    def testStr(self):
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 1/3")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 1/2 - 5/4")
        self.assertEqual(str(self.r3), "[Rectangle] (3) 5/1 - 3/2")
        self.assertEqual(str(self.r4), "[Rectangle] (4) 0/0 - 2/2")

    # Test display method.
    def testDisplay(self):
        """
            More tricky to ckeck than previous methods.
            First we capture what's printed to std.out and then we assertEqual
            with the expected output, given as a string.
        """
        li = [(self.r1, "#\n#\n#\n"),
              (self.r2, "\n\n #####\n #####\n #####\n #####\n"),
              (self.r3, "\n     ###\n     ###\n")]

        for tup in li:
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            tup[0].display()
            sys.stdout = sys.__stdout__
            self.assertEqual(tup[1], capturedOutput.getvalue())

    # Test update method only using *args
    def testUpdateArgs(self):
        self.r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 10/10 - 10/10")
        self.r1.update(89)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 10/10")
        self.r1.update(89, 2)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/10")
        self.r1.update(89, 2, 3)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/3")
        self.r1.update(89, 2, 3, 4)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/10 - 2/3")
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/5 - 2/3")
        self.r1.update(89, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/5 - 2/3")

    # Test update method using only **kwargs
    def testUpdateKwargs(self):
        self.r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 10/10 - 10/10")

        self.r1.update(id=89)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 10/10")

        self.r1.update(height=3)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 10/3")

        new_dict = {'x': 2, 'y': 1}
        self.r1.update(**new_dict)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 2/1 - 10/3")

        full_dict = {'id': 1, 'width': 2, 'height': 3, 'y': 5, 'x': 4}
        self.r1.update(**full_dict)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 4/5 - 2/3")

        extra_vars = {'id': 10, 'width': 2, 'height': 2,
                      'whats': 'this', 'new': 2}
        self.r1.update(**extra_vars)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 4/5 - 2/2")
        self.assertTrue('whats' in self.r1.__dict__ and
                        'new' in self.r1.__dict__)

    # Test update method with *args and **kwargs
    def testUpdateMixed(self):
        self.r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(self.r1), "[Rectangle] (10) 10/10 - 10/10")
        self.r1.update(1, 2, 3, x=4, y=5)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 2/3")
        self.r1.update(0, 2, 3, id=4, height=5)
        self.assertEqual(str(self.r1), "[Rectangle] (0) 10/10 - 2/3")

    def testToDictionary(self):
        for rectangle in [self.r1, self.r2, self.r3, self.r4]:
            rectangle_dic = rectangle.to_dictionary()
            for key, value in rectangle_dic.items():
                self.assertEqual(getattr(rectangle, key), value)
            self.assertEqual(len(rectangle_dic), len(rectangle.__dict__))


if __name__ == "__main__":
    unittest.main()
