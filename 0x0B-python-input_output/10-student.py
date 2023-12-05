#!/usr/bin/python3
"""Contains the clas "Student"""


class Student:
    """class of student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student
        object with the given first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Returns:
            None

        Example Usage:
            student = Student("John", "Doe", 20)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the object attributes into a JSON-like dictionary.

        Args:
            attrs (list, optional):
            A list of attribute names to include
            in the JSON-like dictionary.
            If not provided, all attributes are included.

        Returns:
            dict: A JSON-like dictionary representation
            of the object's attributes. If `attrs` is provided,
            only the specified attributes are included in the dictionary.
        """
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
