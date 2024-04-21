#!/usr/bin/python3
"""importing our base class"""
from models.base import Base
"""class Rectangle that inherits from Base"""


class Rectangle(Base):
    """class Rectangle, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method for our class
        Args:
            self: obj instance
            width: width
            height:height
            x:x
            y:y
            id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """method to get value of width
        Args:
            self: obj instance
        Returns: value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """method that sets value of width
        Args:
            self:obj instance
            value: value to be set
        Raises:
            TypeError: if width not int
            ValueError: width <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """method to return value of height
        Args:
            self: obj instance
        Returns:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """method to set value of height
        Args:
            self:obj instance
            value: value to be set
        Raises:
            TypeError: height not int
            ValueError: height <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method to get value of x
        Args:
            self:obj instance
        Returns:
            value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """method to set x
        Args:
            self: obj instance
            value: value to set
        Raises:
            TypeError: x not int
            ValueError: x < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method to return y
        Args:
            self: obj instance
        Returns:
            value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """method to set y
        Args:
            self: object instance
            value: value to set
        Raises:
            TypeError:y not an int
            ValueError: y < 0

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method to find area"""
        return self.__height * self.__width

    def display(self):
        """method to display shape based on widht and height"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """method to update values of attrs
        Args:
            *args: arguments
            **kwargs: key word args
        """
        if len(args) == 0:
            kwargsKeys = kwargs.keys()
            if 'height' in kwargsKeys:
                self.height = kwargs['height']
            if 'width' in kwargsKeys:
                self.width = kwargs['width']
            if 'x' in kwargsKeys:
                self.x = kwargs['x']
            if 'y' in kwargsKeys:
                self.y = kwargs['y']
            if 'id' in kwargsKeys:
                self.id = kwargs['id']
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

    def to_dictionary(self):
        """return dict rep of a Rectangle"""
        rectDict = {}
        rectDict.update({'x': self.x})
        rectDict.update({'y': self.y})
        rectDict.update({'id': self.id})
        rectDict.update({'height': self.height})
        rectDict.update({'width': self.width})
        return rectDict
