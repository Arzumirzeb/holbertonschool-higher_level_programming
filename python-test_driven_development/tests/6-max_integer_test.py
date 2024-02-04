#!/usr/bin/python3
"""Interactive tests"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_unordered_list(self):
        test_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(test_list), 4)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_max_first(self):
        test_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_end(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_middle(self):
        test_list = [4, 3, 5, 2, 1]
        self.assertEqual(max_integer(test_list), 5)

    def test_max_all_negative(self):
        test_list = [-4, -5, -7, -1]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_max(self):
        test_list = [50]
        self.assertEqual(max_integer(test_list), 50)
