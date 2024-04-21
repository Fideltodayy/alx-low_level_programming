#!/usr/bin/python3
"""importing json module"""
import json
"""class Base. will be base for all shapes"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method for our class"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to return the JSON string rep of list_dictionaries
        Args:
            list_dictionaries: list of dicts
        Returns:
            Json str rep of the list
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """method to write the json str rep of list_objs
        Args:
            list_objs: a list of class instances
        """
        if not list_objs:
            list_objs_json = "[]"
        instances_list = []
        for item in list_objs:
            instances_list.append(item.to_dictionary())
            list_objs_json = cls.to_json_string(instances_list)
            filename = (cls.__name__) + ".json"
            with open(filename, "w", encoding="utf-8") as myFile:
                myFile.write(list_objs_json)

    @staticmethod
    def from_json_string(json_string):
        """method to return list of the json str rep of json_string
        Args:
            json_string: json string
        Returns:
            json str rep of the str passed, or [] if not json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method to return an instance with all attrs already set
        Args:
            dictionary: dict passed in
        Returns: an instance with attrs in the dict
        """
        Rectangle = __import__('rectangle').Rectangle
        rect = Rectangle(12, 21, 32, 43,55)
        rect.update(**dictionary)
        return rect
