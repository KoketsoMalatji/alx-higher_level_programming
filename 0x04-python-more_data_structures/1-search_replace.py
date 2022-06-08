#!/usr/bin/python3
def ssearch_replace(my_list, search, replace):
    return[replace if item == search else item for item in my_list]
