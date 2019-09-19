#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cc = dict.copy(a_dictionary)
    for key in cc:
        cc[key] *= 2
    return cc
