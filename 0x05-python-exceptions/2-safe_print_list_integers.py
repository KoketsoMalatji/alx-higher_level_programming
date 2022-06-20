#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    items = printed_ints = 0
    while True:
        try:
            if items < x:
                print("{:d}".format(my_list[items]), end='')
                items += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            items += 1
