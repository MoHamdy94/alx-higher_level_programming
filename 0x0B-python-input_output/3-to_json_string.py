#!/usr/bin/python3
"""Module 3-to_json"""
import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string representation.

    Args:
        my_obj: The object to be converted.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
