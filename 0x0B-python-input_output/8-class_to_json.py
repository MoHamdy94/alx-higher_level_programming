#!/usr/bin/python3
"""Module 8-class_to_json"""


def class_to_json(obj):
    """
    Returns a dictionary representation of the object's attributes.

    Args:
        obj (object):
        The object for which
        the dictionary representation of attributes needs to be generated.

    Returns:
        dict: A dictionary representation of the input object's attributes.
    """
    return obj.__dict__
