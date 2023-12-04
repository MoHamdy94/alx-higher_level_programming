#!/usr/bin/python3
class MyInt(int):
    """
    MyInt class that inherits from int and inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the equality comparison.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Inverts the inequality comparison.
        """
        return not super().__ne__(other)
