#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int,float): first integer
        b (int, float): second integer. Defaults to 98.
    Raises:
        TypeError: if a, b are not int, float
    Return:
        sum of two integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
