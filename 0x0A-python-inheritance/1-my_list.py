#!/usr/bin/python3
"""My module for 1-my_list"""


class MyList(list):
    """Class for MyList, inherits from list"""
    def print_sorted(self):
        """print sorted list method"""
        print(sorted(self))
