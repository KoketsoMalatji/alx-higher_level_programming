#!/usr/bin/python3
"""Module for 3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is of a sublass of a_class
    Args:
        obj: the object
        a_class: the class we are checking it for
    """
    return isinstance(obj, a_class)
