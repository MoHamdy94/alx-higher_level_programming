#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=""))
            total += 1
            for j in range(i):
                print("nb_print: {}".format(j))
        except (ValueError, TypeError):
            pass
    print()
    return total
