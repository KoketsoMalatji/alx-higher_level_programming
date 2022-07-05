#!/usr/bin/python3
def read_file(filename=""):
    """function that reads and print  text file"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
