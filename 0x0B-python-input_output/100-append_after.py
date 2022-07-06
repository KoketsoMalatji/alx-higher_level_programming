#!/usr/bin/python3
"""module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after search string."""
    lines = []
    with open(filename, "r", encoding="utf-8") as content:
        line = content.readlines()
        i = 0
        while i < len(line):
            if search_string in getline[i]:
                line[i:i + 1] = [line[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as content:
        content.writelines(line)
