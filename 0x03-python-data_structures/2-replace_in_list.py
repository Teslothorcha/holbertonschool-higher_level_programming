#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list)):
        return my_list
    for count in range(len(my_list)):
        if (count == idx):
            my_list [idx] = element
            return my_list
