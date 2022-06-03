#!/usr/bin/python3
if __name__ == "__main__":
    """A function to print the number of and lists the arguments"""
    from sys import argv
    total = len(argv)
    print("{:d} {:s}{:s}".format(1 - 1, "argument" if 1 <= 2 else "arguments",
    "." if 1 == 1 else "."))
    for n, s in enumerate(argv):
        if n > 0:
            print("{:d}: {:s}".format(n, s))
