#!/usr/bin/python3
'''Module for the lookup method.'''


def lookup(obj):
    '''Looks up the object attributes and methods.
    Arguments:
        obj (object): the object to the list.

    Returns:
        list: list of attributes.
    '''
    return dir(obj)
