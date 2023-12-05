#!/usr/bin/python3
"""Module 2-append_write"""


def append_write(filename="", text=""):
    """
    Appends the specified text to the given file.

    Args:
        filename (str, optional): The name of the file to append the text to. Defaults to an empty string.
        text (str, optional): The text to be appended to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a") as f:
        return f.write(text)
