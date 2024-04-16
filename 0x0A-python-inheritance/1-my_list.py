#!/usr/bin/python3
'''The module for the MyList class.'''


class MyList(list):
    '''The custom MyList class.'''
    def print_sorted(self):
        '''Method for printing the sorted list.'''
        print(sorted(self))
