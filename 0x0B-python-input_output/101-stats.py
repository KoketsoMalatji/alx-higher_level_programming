#!/usr/bin/python3
'''module for stats'''


def add_attribute(object, name, value):
    '''this function adds new attr to the obj if possible'''
    if '__dict__' in dir(object):
        object.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
