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
    l = len(text)
    text = text.strip()
    for i in range(0, l):
        if ord(text[i]) == 46 or ord(text[i]) == 63 or ord(text[i]) == 58:
            if ord(text[i]) == 46:
                print(".", end="")
                print()
                print()
                i += 1
            if ord(text[i]) == 63:
                print("?", end="")
                print()
                print()
                i += 1
            if ord(text[i]) == 58:
                print(":", end="")
                print()
                print()
                i += 1
        else:
            print("{:s}".format(text[i]), end="")
