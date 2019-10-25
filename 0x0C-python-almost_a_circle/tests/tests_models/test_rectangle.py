#!/usr/bin/python3

"""set of tests rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import os


class RectangleTest(unittest.TestCase):
    """Tests rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """checks for any docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_class(self):
        '''Testsclass'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_isinstance(self):
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_con_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_float(self):
        with self.assertRaises(TypeError) as e:
            b = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_con_o_arg(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def testinst(self):
        '''Tests instantiation.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

    def test_none(self):
        with self.assertRaises(TypeError) as x:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(x.exception))

    def test_isinstance(self):
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(
            d, {'height': 7, 'id': 1, 'width': 10, 'x': 2, 'y': 8})

if __name__ == '__main__':
    unittest.main()
