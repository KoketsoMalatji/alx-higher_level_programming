#!/usr/bin/python3
'''module for 1-number_of_lines'''


def write_file(filename="", text=""):
    '''writes a string to  file overwrites if exist'''
    with open(filename, mode='w', encoding='utf-8') as f:
        fil = f.write(text)

    return fil
