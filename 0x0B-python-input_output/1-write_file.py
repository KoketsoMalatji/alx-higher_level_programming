#!/usr/bin/python3
"""module for 1-number_of_lines """


def number_of_lines(filename=""):
    """to read # of lines"""
    with open(filename, "r", encoding="utf-8") as content:
        return len(content.readlines())
