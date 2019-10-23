#!/usr/bin/python3
"""base nui test"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class BaseTest(unittest.TestCase):
    """base class
    test
    cases
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
