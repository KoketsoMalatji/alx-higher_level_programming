#!/usr/bin/python3


def uniq_add(my_list=[]):
    success = 0
    for x in set(my_list):
        success += x
    return success
