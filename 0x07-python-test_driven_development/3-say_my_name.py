#!/usr/bin/python3
"""Module for say_my_name method."""
import doctest


def say_my_name(first_name, last_name=""):
    """Print first and last name

    Args:
        first_name (str): first name string
        last_name (str): last name string. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    if not isinstance(first_name, str):
        raise TypeError("First name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last name must be a string")

    print("My name is {:s} {:s}".format(first_name, Last_name))


if __name__ == "__main__":
    doctest.testfile("tests/3-say_my_name.txt")
