#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of all the attributes and methods of an object.

    Args:
        obj (any object): The object for which we want to retrieve the attributes and methods.

    Returns:
        attributes (list): A list of all the attributes and methods of the input object.
    """
    return dir(obj)
