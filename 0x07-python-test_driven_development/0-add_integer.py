#!/usr/bin/python3
"""
This function will add two values
casted values if necessary (int/float)
and return the addition
"""


def add_integer(a, b=98):
    """
    check if args are ints to add'em'
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
