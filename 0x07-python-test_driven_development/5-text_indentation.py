#!/usr/bin/python3
"""
This divide a matrix
into a given number
and return a new matrix
"""


def text_indentation(text):
    """
    checks data accuracy to perfom name generation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for ident in text:
        if ord(ident) == 46 or ord(ident) == 63:
            if ord(ident) == 46:
                print(".", end="")
                print()
                print()
            if ord(ident) == 63:
                print("?", end="")
                print()
                print()
        else:
            print("{:s}".format(ident), end="")
    print()
