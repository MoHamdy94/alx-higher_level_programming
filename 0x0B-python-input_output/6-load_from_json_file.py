#!/usr/bin/python3
"""Module 6-load_from_json"""
import json


def load_from_json_file(filename):
    """
    Loads data from a JSON file and returns it.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        The JSON data loaded from the file.

    Example Usage:
        data = load_from_json_file('data.json')
        print(data)
    """
    with open(filename) as f:
        data = json.load(f)
        return data
