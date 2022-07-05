#!/usr/bin/python3
'''modele for to_json_string'''


import json


def to_json_string(my_obj):
    '''returns the json format of the obj'''
    return json.dumps(my_obj)
