#!/usr/bin/python3
"""module inherits"""


def inherits_from(obj, a_class):
    """
    Check if an object
    is an instance of a class and if it inherits from that class.

    Args:
        obj: The object to be checked.
        a_class: The class to check if the object inherits from.

    Returns:
        True if obj is an instance of a_class and does not equal a_class.
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
