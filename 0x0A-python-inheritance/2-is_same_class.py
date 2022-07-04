#!/usr/bin/python3
'''module for 2-is_same_class'''


def is_same_class(obj, a_class):
    '''this function returns true if obj is an instance of a_class'''
    return type(obj) is a_class
