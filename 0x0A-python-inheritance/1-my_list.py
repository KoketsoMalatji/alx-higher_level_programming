#!/usr/bin/python3
'''module for 1-my_list.py'''


class MyList(list):
    """Defining list class"""

    def print_sorted(self):
        """print sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
