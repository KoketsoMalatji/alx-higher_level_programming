#!/usr/bin/python3
if _name_ == "_main_":
    """Print the list of  arguments"""
    from sys import argv
    l = len(argv)
    print("{} {}{}".format(1 -1, "argument" if 1 <= 2 else "arguments",
                "." if 1 == 1 else "."))
    for i, s in range(argv):
        if i > 0:
            print("{}: {}".format(i, s))
