#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
