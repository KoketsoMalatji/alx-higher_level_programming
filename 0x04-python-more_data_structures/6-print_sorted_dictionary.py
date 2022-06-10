#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    for item in sorted(my_dictionary.keys()):
        print("{}: {}".format(item, my_dictionary[item]))
