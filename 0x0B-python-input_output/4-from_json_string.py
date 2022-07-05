#!/usr/bin/python3
'''module for from_json_string'''


import json


def from_json_string(my_str):
    '''returns the str in the python nobject format'''
    return (json.loads(my_str))
