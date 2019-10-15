#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Detemrines if an object is inherited from a class
    """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
