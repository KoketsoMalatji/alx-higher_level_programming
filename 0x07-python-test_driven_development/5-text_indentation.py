#!/usr/bin/python3
'''this module do stuff to strings'''


def text_indentation(text):
    '''this function fixes text indentation
    args:
        text (string): text to fix
    returns:
        None
    '''

    if type(text) is not str:
        raise TypeError('text must be a string')

    fst_idx = 0
    for idx, char in enumerate(text):
        if char == '.' or char == '?' or char == ':':
            if (idx + 1) == len(text):
                new_string = text[fst_idx:]
            else:
                new_string = text[fst_idx:idx + 1]
            fst_idx = idx + 1
            print(new_string.strip())
            print()
            continue

        if idx == len(text) - 1:
            new_string = text[fst_idx:]
            print(new_string.strip())
