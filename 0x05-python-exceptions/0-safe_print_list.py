#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    y = 0
    try:
        for s in range(x):
            print("{}".format(my_list[s]), end="")
            y = y + 1
        print()
    except IndexError:
        print()
        pass
    return y
