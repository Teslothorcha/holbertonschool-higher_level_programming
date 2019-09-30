#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    f = 0
    try:
        c = a / b
        return(c)
    except (TypeError, ZeroDivisionError):
        f = 1
        return(None)
    finally:
        if f == 1:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(c))
