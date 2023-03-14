#!/usr/bin/python3
"""
    This module provides some basic tests for the Base class.
"""


import unittest
import json
import random
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

    def testEmptyToJsonStr(self):
        empty = Base.to_json_string(None)
        self.assertEqual(type(empty), str)
        self.assertEqual(empty, "[]")
        empty = Base.to_json_string([])
        self.assertEqual(type(empty), str)
        self.assertEqual(empty, "[]")

    def testRecToJsonStr(self):
        r1 = Rectangle(random.randrange(1, 100), random.randrange(1, 100),
                       random.randrange(1, 100), random.randrange(1, 100),
                       random.randrange(100, 500))

        r1_dic = r1.to_dictionary()
        rjson = Base.to_json_string([r1_dic])
        self.assertTrue(type(rjson) is str)
        deserialized = json.loads(rjson)
        for dic in deserialized:
            for key, value in dic.items():
                self.assertEqual(getattr(r1, key), value)
                self.assertEqual(r1_dic[key], dic[key])
                del r1_dic[key]
            self.assertEqual(len(r1_dic), 0)

        r2, r3 = Rectangle(1, 2, 3, 4, 5), Rectangle(5, 4, 3, 2, 1)
        rec_li = [r1, r2, r3]
        dic_li = [r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        rjson = Base.to_json_string(dic_li)
        deserialized = json.loads(rjson)
        for idx, dic in enumerate(deserialized):
            for key, value in dic.items():
                self.assertEqual(getattr(rec_li[idx], key), value)
                self.assertEqual(dic_li[idx][key], dic[key])
                del dic_li[idx][key]
            self.assertEqual(len(dic_li[idx]), 0)

    def testSquareToJsonStr(self):
        s1 = Square(random.randrange(1, 100), random.randrange(1, 100),
                    random.randrange(1, 100), random.randrange(1, 100))

        s1_dic = s1.to_dictionary()
        rjson = Base.to_json_string([s1_dic])
        self.assertTrue(type(rjson) is str)
        deserialized = json.loads(rjson)
        for dic in deserialized:
            for key, value in dic.items():
                self.assertEqual(getattr(s1, key), value)
                self.assertEqual(s1_dic[key], dic[key])
                del s1_dic[key]
            self.assertEqual(len(s1_dic), 0)

        s2 = Square(random.randrange(1, 100), random.randrange(1, 100),
                    random.randrange(1, 100), random.randrange(1, 100))
        s3 = Square(random.randrange(1, 100), random.randrange(1, 100),
                    random.randrange(1, 100), random.randrange(1, 100))
        sq_li = [s1, s2, s3]
        dic_li = [s1.to_dictionary(), s2.to_dictionary(), s3.to_dictionary()]
        rjson = Base.to_json_string(dic_li)
        deserialized = json.loads(rjson)
        for idx, dic in enumerate(deserialized):
            for key, value in dic.items():
                self.assertEqual(getattr(sq_li[idx], key), value)
                self.assertEqual(dic_li[idx][key], dic[key])
                del dic_li[idx][key]
            self.assertEqual(len(dic_li[idx]), 0)

    def testJsonToFileEmpty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            contents = f.read()
        self.assertEqual(contents, "[]")

        Square.save_to_file([])
        with open("Square.json", 'r', encoding='utf-8') as f:
            contents = f.read()
        self.assertEqual(contents, "[]")

    def testJsonToFileRec(self):
        r1 = Rectangle.createRandomRectangle()
        r2 = Rectangle.createRandomRectangle()
        r3 = Rectangle.createRandomRectangle()

        rec_li = [r1, r2, r3]
        Rectangle.save_to_file(rec_li)
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            contents = f.read()
        objects = json.loads(contents)
        copy = [objects[i].copy() for i in range(len(objects))]
        for idx, dir in enumerate(objects):
            for key, value in dir.items():
                self.assertEqual(getattr(rec_li[idx], key), value)
                del copy[idx][key]
            self.assertEqual(len(copy[idx]), 0)

    def testJsonToFileSquare(self):
        s1 = Square.createRandomSquare()
        s2 = Square.createRandomSquare()
        s3 = Square.createRandomSquare()

        sq_li = [s1, s2, s3]
        Square.save_to_file(sq_li)
        with open("Square.json", 'r', encoding='utf-8') as f:
            contents = f.read()
        objects = json.loads(contents)
        copy = [objects[i].copy() for i in range(len(objects))]
        for idx, dir in enumerate(objects):
            for key, value in dir.items():
                self.assertEqual(getattr(sq_li[idx], key), value)
                del copy[idx][key]
            self.assertEqual(len(copy[idx]), 0)


if __name__ == '__main__':
    unittest.main()
