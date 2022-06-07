#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for n in range(len(my_string)):
        if (my_string[n] != 'c' and my_string[n] != 'C'):
            new += my_string[n]
            return new
