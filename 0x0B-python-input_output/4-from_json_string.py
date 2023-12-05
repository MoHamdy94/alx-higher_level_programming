#!/usr/bin/python3
"""Module 4-from_json"""
import json


def from_json_string(my_str):
    """
    Parse a JSON string and return a Python object.

    Args:
        my_str (str): A string representing a JSON object.

    Returns:
        object: A Python object representing the parsed JSON data.
    """
    return json.loads(my_str)
