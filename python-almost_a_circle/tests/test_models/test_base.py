#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """Instances for test"""
        self.b1 = Base()
        self.b2 = Base(None)
        self.b3 = Base(3)
        self.b4 = Base(-4)
        self.b5 = Base("Messimde Messim")

        self.json_string_1 = Base.to_json_string(None)
        self.json_string_2 = Base.to_json_string([])
        self.json_string_3 = Base.to_json_string([{"id": 1}])

        self.json_string_4 = Base.from_json_string(None)
        self.json_string_5 = Base.from_json_string('[{"id": 1}]')

    # Testing Instances
    def test_id_checker(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, -4)
        self.assertEqual(self.b5.id, "Messimde Messim")

    # JSON methods testing
    def test_json_string_methods(self):
        self.assertEqual(self.json_string_1, "[]")
        self.assertEqual(self.json_string_2, "[]")
        self.assertEqual(self.json_string_3, '[{"id": 1}]')
        self.assertEqual(self.json_string_5, [{"id": 1}])
        self.assertEqual(self.json_string_4, [])
