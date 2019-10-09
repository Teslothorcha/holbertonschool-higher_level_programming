#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max(self):
        self.assertEqual(max_integer([]), None)

    def test_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
    def test_max(self):
        self.assertEqual(max_integer([4, 2, 2, 2]), 4)
    def test_max(self):
        self.assertEqual(max_integer([4, 4, 6, 4, 4]), 6)
