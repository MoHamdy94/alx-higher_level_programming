#!/usr/bin/python3
def read_file(filename=""):
    """
    Read the contents of a file and print each line.

    Args:
        filename (str, optional):
        The name of the file to be read. Defaults to "".

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
