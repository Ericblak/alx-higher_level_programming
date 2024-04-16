#!/usr/bin/python3
"""
This contains the class MyInt
"""


class MyInt(int):
    """The rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """This creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, a):
        """what was != is now =="""
        return int(self) != a

    def __ne__(self, a):
        """what was == is now !="""
        return int(self) == a
