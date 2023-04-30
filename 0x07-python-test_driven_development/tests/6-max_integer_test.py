#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for function max_integer"""

    def test_max_integer(self):
        """Tests returns values for normal and specific cases"""
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([2, 1, 0]), 2)
        self.assertEqual(max_integer([0, 99999999, 2]), 99999999)
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-99999, 2, 0]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
