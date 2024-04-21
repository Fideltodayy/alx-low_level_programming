#!/usr/bin/python3
"""importing modules"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

"""class to test our classes"""


class TestClasses(unittest.TestCase):
    """class for testing our methods"""

    def setUp(self):
        """setup method"""
        self.rect = Rectangle(3, 43, 1, 9, 22)

    def test_to_json_string(self):
        """test"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_dict = json.loads('[{"x": 2, "width": 10, "id": 1, "height": 7, "y":8}]')
        actual_dict = json.loads(json_dictionary)
        self.assertEqual(actual_dict, expected_dict)
        new_dict = Base.to_json_string([])
        self.assertEqual(new_dict, "[]")

    def test_from_json_string(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
