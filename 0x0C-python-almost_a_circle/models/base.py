#!/usr/bin/python3
"""
This module contains the "Base" class
"""
import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of
        the Base class and assigns a unique ID to it.

        :param id: An integer representing
        the ID of the instance. If not provided, a unique ID will be assigned.
        :type id: int, optional

        :return: None
        :rtype: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): A list
            of dictionaries to be converted into a JSON string.

        Returns:
            str: A JSON string representing the input list of dictionaries.

        Example:
            >>> data = [
            ...     {"name": "John", "age": 30},
            ...     {"name": "Jane", "age": 25}
            ... ]
            >>> json_string = to_json_string(data)
            >>> print(json_string)
            [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        """
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        li = []
        try:
            with open(filename, 'r') as f:
                li = cls.from_json_string(f.read())
            for i, e in enumerate(li):
                li[i] = cls.create(**li[i])
        except:
            pass
        return li
