#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _description_
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size ** 2
