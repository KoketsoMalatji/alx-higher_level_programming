#!/usr/bin/python3
"""module for mylist"""


class MyList(list):
    """my own class: MyList, inherits from list"""
    def print_sorted(self):
        """print sorted list method"""
        print(sorted(self))
