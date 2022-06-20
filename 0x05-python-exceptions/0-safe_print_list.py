#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    try:
        while value is not x:
            print(my_list[value], end='')
            value = value + 1
    except IndexError:
        None
    print()
    return value
