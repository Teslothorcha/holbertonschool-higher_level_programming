#!/usr/bin/python3
"""rectangle uni test"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os

class RectangleTest(unittest.TestCase):
    """rectangle
    test
    cases"""

    def test_class_docstring(self):
        """first kin
        of
        tests"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)
