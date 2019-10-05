#!/usr/bin/python3
"""
This divide a matrix
into a given number
and return a new matrix
"""


def print_square(size):
    """
    checks data accuracy to perfom name generation
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise ValueError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for squ in range(size):
        print('#' * size)
