#!/usr/bin/python3
"""Module for say_my_name method."""


def say_my_name(first_name, last_name=""):
    """Print first and last name

    Args:
        first_name (str): first name string
        last_name (str): last name string. Defaults to "".

    Raises:
        TypeError: First name must be a string
        TypeError: Last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
