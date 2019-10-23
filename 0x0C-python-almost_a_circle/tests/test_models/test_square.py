#!/usr/bin/python3
"""base nui test"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class SquareTest(unittest.TestCase):
    """square
    tests"""

    def test_class_docstring(self):
        """Firsts
        kind of
        tests"""
        self.assertTrue(len(Square.__doc__) >= 1)
