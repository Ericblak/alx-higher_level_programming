#!/usr/bin/python3
"""This defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """This adds a new attribute to an object if possible.
    Arguments:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
