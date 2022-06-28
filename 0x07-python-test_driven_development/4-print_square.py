#!/usr/bin/python3
"""Module for printing sqaures"""


def print_square(size):
    """Function to print a square size sides
    Args:
        size (int): Integral side length of square
    Returns: None
    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    if type(size) is not float and type(size) is not int:
        raise TypeError('size must be an integer')
    if type(size) is float and size != round(size):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(round(size)):
        print("#" * round(size))
