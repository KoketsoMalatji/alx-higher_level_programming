#!/usr/bin/python3
ef new_in_list(my_list, idx, element):
    isinstance = len(my_list)

    new_list = my_list[:]

    if 0 <= idx < isinstance:
        new_list[idx] = element

    return (new_list)
