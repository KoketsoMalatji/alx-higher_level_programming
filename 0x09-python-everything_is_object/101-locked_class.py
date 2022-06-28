#!/usr/bin/python3
'''A class that rejcts __dict__ and uses slots instead'''


class LockedClass:
    '''The locked class'''

    __slots__ = "first_name"
