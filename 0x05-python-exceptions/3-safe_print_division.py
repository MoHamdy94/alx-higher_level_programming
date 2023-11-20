#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        answer = a / b
    except (ZeroDivisionError, FloatingPointError):
        answer = None
    finally:
        print("Inside result: {}".format(a, b, answer))
