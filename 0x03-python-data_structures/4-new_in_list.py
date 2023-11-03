#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lists = my_list[:]
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        new_lists[idx] = element
        return new_lists
        return my_list
