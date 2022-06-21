#!/usr/bin/python3
def safe_print_list(my_list=[], n=0):
    result = 0
    for i in range(n):
        try:
            print(my_list[i], end='')
            result += 1
        except IndexError:
            break
    print('')
    return result
