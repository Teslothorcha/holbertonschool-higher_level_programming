#!/usr/bin/python3
"""
This function will
show the attributes and
methods of an object
"""


def lookup(obj):
    """
     obj is the instance  to be avaluated
    """
    l = []
    l = dir(obj)
    return l
