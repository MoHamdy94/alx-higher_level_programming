#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for integer in my_list:
        if max is None or integer > max:
            max = integer
    return max
