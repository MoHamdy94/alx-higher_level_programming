#!/usr/bin/python3
"""Module 1-write_file
"""


def write_file(filename="", text=""):
    """Write a file with the given filename
    and content.
    If no arguments are provided, it will create an empty file.
    """

    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
