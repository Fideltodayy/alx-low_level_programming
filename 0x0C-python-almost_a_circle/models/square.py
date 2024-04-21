#!/usr/bin/python3
"""imporing relevant modules"""
from models.rectangle import Rectangle
"""class Square, inherits from Rectangle."""


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method for str"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """method getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """method setter for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to update values of attrs
        Args:
            args: arguments
            kwargs: keyword args
        """
        if len(args) == 0:
            kwargsKeys = kwargs.keys()
            if 'size' in kwargsKeys:
                self.size = kwargs['size']
            if 'x' in kwargsKeys:
                self.x = kwargs['x']
            if 'y' in kwargsKeys:
                self.y = kwargs['y']
            if 'id' in kwargsKeys:
                self.id = kwargs['id']
        else:
            length = len(args)
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]

    def to_dictionary(self):
        """method to return the dict rep of a Square"""
        squareDict = super().to_dictionary()
        del squareDict['height']
        del squareDict['width']
        squareDict.update({'size': self.size})
        return squareDict
