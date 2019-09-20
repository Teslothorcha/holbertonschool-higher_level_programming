#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for count in list(a_dictionary.keys()):
            if a_dictionary[count] == value:
                a_dictionary.pop(count, None)
    return a_dictionary
