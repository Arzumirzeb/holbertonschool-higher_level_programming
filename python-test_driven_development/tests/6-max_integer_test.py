#!/usr/bin/python3
"""Interactive tests"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_ordered_list(self):
        ordered_list = [1, 3, 2, 4]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_max_beggining(self):
        test_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_ending(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_all_negative(self):
        test_list = [-4, -5, -7, -1]
        self.assertEqual(max_integer(test_list), 4)

    def test_one(self):
        test_list = [50]
        self.assertEqual(max_integer(test_list), 50)

    def test_floats(self):
        test_list = [4.12, 3.45, 2.76, 1.81]
        self.assertEqual(max_integer(test_list), 4)

    def test_strings(self):
        test_list = ["bir", "iki", "yeddi", "doqquz"]
        self.assertEqual(max_integer(test_list), 4)
