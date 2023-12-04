#!/usr/bin/python3
"""Module 6-base_geometry."""


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
