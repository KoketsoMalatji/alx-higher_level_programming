#!/usr/bin/python3
def best_score(my_dictionary):
    if my_dictionary is None or my_dictionary == {}:
        return None
    best = max(my_dictionary.values())
    for key, value in my_dictionary.items():
        if value is best:
            return key
