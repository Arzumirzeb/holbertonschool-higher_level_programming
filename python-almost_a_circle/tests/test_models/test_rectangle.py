#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os

class TestRectangle(unittest.TestCase):

    def setUp(self):
        """Instances for rectangle"""
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(7, 7, 7, 7)
        self.r4 = Rectangle(1, 2, 3, 64 ,5)
    def test_checker(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.y, 7)
        self.assertEqual(self.r4.id, 5)

        """Type Error"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        """Value Error"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
      
    """Testing area"""
    def test_area(self):
        self.assertEqual(self.r1.area(), 2)

    """Testing __str__"""
    def test_str(self):
        self.assertEqual(self.r4.__str__(), "[Rectangle] (5) 3/64 - 1/2")

    def test_display(self):
        output = "#\n#\n"
        with patch("sys.stdout", new=StringIO()) as o:
            self.r1.display()
            self.assertEqual(o.getvalue(), output)
        output = "   #\n   #\n"
        with patch("sys.stdout", new=StringIO()) as o:
            self.r2.display()
            self.assertEqual(o.getvalue(), output)

