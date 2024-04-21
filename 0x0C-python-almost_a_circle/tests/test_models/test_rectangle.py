"""importing modules"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """setup method"""
        self.rect = Rectangle(3, 43, 1, 9, 22)

    def test_init(self):
        """test constructor method"""
        self.assertEqual(self.rect.width, 3)
        self.assertEqual(self.rect.id, 22);
        self.assertEqual(self.rect.x, 1)

    def test_width(self):
        """method to test width method"""
        self.assertEqual(self.rect.width, 3)
        self.rect.width = 32
        self.assertEqual(self.rect.width, 32)

        with self.assertRaises(TypeError):
            self.rect.width = "89"
        with self.assertRaises(ValueError):
            self.rect.width = -32

    def test_height(self):
        """method to test height"""
        self.assertEqual(self.rect.height, 43)
        self.rect.height = 47
        self.assertEqual(self.rect.height, 47)

        with self.assertRaises(TypeError):
            self.rect.height = "32"
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_x(self):
        """method to test x"""
        self.assertEqual(self.rect.x, 1)
        self.rect.x = 30
        self.assertEqual(self.rect.x, 30)
        with self.assertRaises(TypeError):
            self.rect.x = "39"
        with self.assertRaises(ValueError):
            self.rect.x = -2

    def test_y(self):
        """method to test y"""
        self.assertEqual(self.rect.y, 9)
        self.rect.y = 98
        self.assertEqual(self.rect.y, 98)
        with self.assertRaises(TypeError):
            self.rect.y = "32"
        with self.assertRaises(ValueError):
            self.rect.y = -9

    def test_id(self):
        """testing for id attr"""
        self.assertEqual(self.rect.id, 22)
        self.rect.id = 4
        self.assertEqual(self.rect.id, 4)

    def test_area(self):
        """method to test area method"""
        self.assertEqual(self.rect.area(), 129)
        self.rect.width = 3
        self.rect.height = 8
        self.assertEqual(self.rect.area(), 24)

    def test_str(self):
        """test the str() method"""
        self.assertEqual(str(self.rect), '[Rectangle] (22) 1/9 - 3/43')

    def test_update(self):
        """method to test update method"""

        self.rect.update(height=7, width=12, id=89, y=1)
        self.assertEqual(self.rect.height, 7)
        self.assertEqual(self.rect.id, 89)

    def test_to_dictionary(self):
        #convert dict to str first to maintaien keys order
        mydictStr = json.dumps(self.rect.to_dictionary())
        self.assertEqual(mydictStr, '{"x": 1, "y": 9, "id": 22, "height": 43, "width": 3}')
