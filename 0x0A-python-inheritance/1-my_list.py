#!/usr/bin/python3
"""Module 1-my_list.
Creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList inherits from list."""
    class MyList(list):
        """
        A subclass of the built-in
        list class in Python that adds a new method called print_sorted.

        Example Usage:
        my_list = MyList([3, 1, 2])
        my_list.print_sorted()

        Output:
        [1, 2, 3]
        """

        def print_sorted(self):
            """
            Prints the sorted version of the list.
            """
            sorted_list = self[:]
            sorted_list.sort()
            print("{}".format(sorted_list))
