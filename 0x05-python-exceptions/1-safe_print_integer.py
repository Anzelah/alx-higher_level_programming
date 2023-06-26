#!/usr/bin/python3
def safe_print_integer(value):
    try:
        case = int(value)
        print("{:d}".format(case))
        return True
    except ValueError:
        return False
