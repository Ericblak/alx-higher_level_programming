#!/usr/bin/python3
""" empty class Rectangle defining a rectangle
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
        """ height
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

    def area(self):
        """ returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimiter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))
