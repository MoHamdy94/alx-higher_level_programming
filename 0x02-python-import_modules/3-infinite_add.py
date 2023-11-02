#!/usr/bin/python3
import sys

if __name__ == '__main__':
    # Cast all arguments into integers.
    arguments = [int(argument) for argument in sys.argv[1:]]

    # Calculate the sum of all arguments.
    sum = 0
    for argument in arguments:
        sum += argument

    # Print the sum.
    print(sum, end='\n')
