#!/usr/bin/python3
"""Module for 1-my_lis"""


class MyList(list):
    """my own class: MyList, inherits from list"""
    def print_sorted(self):
        """print sorted list method"""
        print(sorted(self))
