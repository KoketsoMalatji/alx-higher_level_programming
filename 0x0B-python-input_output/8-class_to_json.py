#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """returns dict descriotion of obj"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
