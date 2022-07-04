#!/usr/bin/python3
'''module for 1-my_list'''


class MyList(list):
    """class utilizing list class"""

    def print_sorted(self):
        """print sorted list"""
        my_list = list.copy(self)
        list.sort(my_list)
        print(my_list)
