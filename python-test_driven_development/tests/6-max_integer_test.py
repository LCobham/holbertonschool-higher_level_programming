#!/usr/bin/python3
"""
    Module to test the ``max_integer`` module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTesting(unittest.TestCase):
    """Class to test the function max_integer"""
    def test_emptyList(self):
        self.assertIsNone(max_integer([]), None)

    def test_maxInMiddle(self):
        self.assertEqual(max_integer([1, 7, 5, 4, 3, 5]), 7)
        self.assertEqual(max_integer([100, 26635, 1e3, 2.6]), 26635)
        self.assertEqual(max_integer([-2000, -154, 3, 4, -float('inf')]), 4)

    def test_maxAtBeginning(self):
        self.assertEqual(max_integer([1, 0, -1]), 1)
        self.assertEqual(max_integer([1e15, 277778, 2, -float('inf')]), 1e15)

    def test_maxAtEnd(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([-15, 40005, 20, 1, 3, 5, 7, 1e15]), 1e15)

    def test_oneElementList(self):
        self.assertEqual(max_integer([3]), 3)

    def test_noInput(self):
        self.assertIsNone(max_integer(), None)

    def test_wrongInputType(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})
        self.assertRaises(TypeError, max_integer, {1, 3, 4, 7, 2})

    def test_wrongListMemberType(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "yes", "no"])


if __name__ == '__main__':
    unittest.main()
