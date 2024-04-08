#!/usr/bin/python3
""" empty class Rectangle defines a rectangle
"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, val):
        """ width setter
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """ height setter
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
