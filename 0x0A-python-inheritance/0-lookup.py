#!/usr/bin/python3
"""Module 0-lookup.
Finding a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    The function "lookup" returns
    a list of all the attributes and methods of an object.
    :param obj: The `obj` parameter
    is an object that you want to inspect and retrieve its attributes
    and methods
    :return: The `lookup` function
    returns a list of all the attributes and methods of the `obj` object.
    """
    return dir(obj)
