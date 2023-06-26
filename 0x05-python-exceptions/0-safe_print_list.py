#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        for i in my_list:
            if length < x:
                print(i, end='')
                length += 1
        print()
        return (length)
    except Exception:
        print("An unknown  error occured")
