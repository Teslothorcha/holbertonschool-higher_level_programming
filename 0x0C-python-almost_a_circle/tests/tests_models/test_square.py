#!/usr/bin/python3

"""
square class set of unitestts
"""
import os
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """especific square class tests"""

    def setUp(self):
        """set ups tests"""
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """checks for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def tearDown(self):
        """ deletes once proved"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_first_s(self):
        s = Square(4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_cllass(self):
        '''checks correct class'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_second_s(self):
        r1 = Square(15, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 15)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)

    def test_dad(self):
        '''Tests inheritance'''
        self.assertTrue(issubclass(Square, Base))

    def test_priv_att(self):
        b = Square(15, 8, 50, 8)
        d = {"_Rectangle__width": 15, "_Rectangle__height": 15,
             "_Rectangle__x": 8, "_Rectangle__y": 50, "id": 8}
        self.assertEqual(b.__dict__, d)

    def test_bob(self):
        '''Tests constructor '''
        with self.assertRaises(TypeError) as e:
            b = Square()
            st = "__init__() missing 1 required positional argument: 'size'"
            self.assertEqual(str(e.exception), st)

    def test_none(self):
        with self.assertRaises(TypeError) as e:
            b = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_more_arg(self):
        '''Tests constructor args input'''
        with self.assertRaises(TypeError) as e:
            b = Square(6, 6, 6, 6, 6)
            st = "__init__() takes from 2 to 5 positional arguments but 6 \
            were given"
            self.assertEqual(str(e.exception), st)

    def test_fuck_args(self):
        """at ñeast 1 args needed"""
        with self.assertRaises(TypeError) as e:
            b = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception))

    def test_init_dict(self):
        '''Tests instantiation.'''
        b = Square(5, 10, 15)
        di = {'_Rectangle__height': 5, '_Rectangle__width': 5,
              '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(b.__dict__, di)

        b = Square(5, 10, 15, 20)
        di = {'_Rectangle__height': 5, '_Rectangle__width': 5,
              '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(b.__dict__, di)

    def test_zerooo(self):
        b = Square(6, 0)
        self.assertEqual(b.x, 0)
        with self.assertRaises(ValueError) as e:
            r = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        b = Square(1, 0, 0, 0)
        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 0)
        self.assertEqual(b.id, 0)

    def test_save_to_file(self):
        r1 = Square(10, 7, 2)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        res = '[{"x": 7, "y": 2, "size": 10, "id": 1},' + \
              ' {"x": 4, "y": 0, "size": 2, "id": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

if __name__ == '__main__':
    unittest.main()
