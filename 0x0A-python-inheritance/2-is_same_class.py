#!/usr/bin/python3
"""module to check is same class"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class.

    Args:
        obj: An object of any class.
        a_class: A class.

    Returns:
        True if the obj belongs to the a_class, False otherwise.
    """
    return True if type(obj) is a_class else False
