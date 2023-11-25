#!/usr/bin/python3
import doctest


def text_indentation(text):
    """text indentaion

    Args:
        text (str): text to be indented

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    doctest.testfile("tests/5-text_indentation.txt")
