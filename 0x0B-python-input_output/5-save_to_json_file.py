#!/usr/bin/python3
"""Module 5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Args:
        my_obj (object): The Python object to be saved as JSON.
        filename (str):
        The name of the JSON file to be created or overwritten.

    Returns:
        None

    Example Usage:
        my_obj = {"name": "John", "age": 30}
        filename = "data.json"
        save_to_json_file(my_obj, filename)
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
