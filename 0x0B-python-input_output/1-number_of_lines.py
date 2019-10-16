#!/usr/bin/python3
def number_of_lines(filename=""):
    c = 0
    with open(filename) as file:
        for line in file:
            line = file.readline()
            if line[-1:] == '\n':
                c += 1
            c += 1
    return c
