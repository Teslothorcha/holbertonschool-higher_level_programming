#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for count in range(0, x):
            print(my_list[count], end="")
        print()
        return(count + 1)
    except IndexError:
        print()
        return(count)
