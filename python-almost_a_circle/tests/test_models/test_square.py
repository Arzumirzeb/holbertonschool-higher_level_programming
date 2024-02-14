#!/usr/bin/python3


import unittest
from models.square import Square
from unittest.mock import patch
from io import StringIO
import os


class TestSquare(unittest.TestCase):

    def setUp(self):
        """Instances for Square"""
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 4)
    def test_checker(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.id, 4)

        """Type Error"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        """Value Error"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

