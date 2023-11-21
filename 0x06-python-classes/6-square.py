#!/usr/bin/python3
"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('5-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """

    def __init__(self, size=0):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size.
                  Has a default value of 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Square setter and getter for __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size private attribute value.

        Validates the assignment of the size private attribute.

        Arg:
        value: the value to be set.

        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position private attribute value.

        Returns:
            The position private attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position private attribute value.

        Validates the assignment of the position private attribute.

        Arg:
            value: the value to be set
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A public object method.

        Returns:
            The current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Displays the square object with # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
