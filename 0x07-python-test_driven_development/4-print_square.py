#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Print square

    Args:
        size (int): size of square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
