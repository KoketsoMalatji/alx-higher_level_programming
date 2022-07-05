#!/usr/bin/python3
'''module for 2-append_write'''


def append_write(filename="", text=""):
    '''appends text to a file'''
    with open(filename, mode='a', encoding='utf-8') as f:
        fil = f.write(text)
    return fil
