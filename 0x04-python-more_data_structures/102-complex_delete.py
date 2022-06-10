#!/usr/bin/python3
def complex_delete(my_dictionary, value):
    targets = []
    for key, key_value in my_dictionary.items():
        if key_value is value:
            targets.append(key)
    for j in targets:
        del my_dictionary[j]
    return(my_dictionary)
