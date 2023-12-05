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

    def to_json(self, attrs =None):
        return self.__dict__
