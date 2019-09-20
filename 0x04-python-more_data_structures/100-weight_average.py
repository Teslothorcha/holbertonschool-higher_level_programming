#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    final = 0
    wei = 0
    for count in my_list:
        final += count[0] * count[1]
        wei += count[1]
    return final/wei
