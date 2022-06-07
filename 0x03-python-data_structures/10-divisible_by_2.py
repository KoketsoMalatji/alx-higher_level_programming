#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_div = []
    if my_list:
        for element in my_list:
            check_div.append(False if element % 2 else True)
    return check_div
