#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if 0 <= idx > (len(my_list)):
        return my_list
    new_list = [j for j in my_list]
    new_list[idx] = element
    return new_element
