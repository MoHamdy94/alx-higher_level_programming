#!/usr/bin/python3
"""Module 7-base_geometry."""


class BaseGeometry:
    """
    A base class that provides a blueprint for other geometry classes.

    Methods:
    - area(): Raises an exception indicating that it is not implemented.
    """

    def area(self):
        """
        Placeholder method
        for subclasses to override
        and provide their own implementation of calculating the area.

        Raises:
        - Exception: Indicates that the method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates whether a given value
        is an integer and whether it meets certain conditions.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Returns:
            None: If the value is valid.

        Raises:
            False: If the name parameter is not a string.
            TypeError: If the value parameter is not an integer.
            ValueError: If the value parameter is less than or equal to 0.
        """
        if type(value) is not int:
            return TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            return ValueError("{:s} must be greater than 0".format(name))
