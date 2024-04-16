#!/usr/bin/python3
'''The module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''The method to compute this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''The method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
