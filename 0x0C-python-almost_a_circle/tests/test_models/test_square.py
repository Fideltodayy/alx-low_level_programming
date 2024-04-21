#!usr/bin/python3
"""importing modules"""
import unittest
import json
from models import square


class TestSquare(unittest.TestCase):
    """class to test square class methods"""
    
    def setUp(self):
        """setup method"""
        self.square = square.Square(9, 12, 63, 11)

    def test_id(self):
        """test method for id"""
        self.assertEqual(self.square.id, 11)
        self.square.id = 4
        self.assertEqual(self.square.id, 4)

    def test_area(self):
        """test for area method"""
        self.assertEqual(self.square.area(), 81)
        self.square.size = 5
        self.assertEqual(self.square.area(), 25)

    def test_size(self):
        """method to test size"""
        self.assertEqual(self.square.size, 9)
        self.square.size = 42
        self.assertEqual(self.square.size, 42)

        with self.assertRaises(TypeError):
            self.square.size = "32"
        with self.assertRaises(ValueError):
            self.square.size = -8

    def test_update(self):
        """testing update method"""
        self.square.update(89, 12, 18, 1)
        self.assertEqual(self.square.height, 12)
        self.assertEqual(self.square.x, 18)
        self.assertEqual(self.square.id, 89)

    def test_to_dictionary(self):
        """test method"""
        s1_dict = self.square.to_dictionary()
        self.assertEqual(s1_dict, {'id': 11, 'x': 12, 'size': 9, 'y': 63})

    def test_str(self):
        """testing __str__ method"""
        self.assertEqual(str(self.square), '[Square] (11) 12/63 - 9')
