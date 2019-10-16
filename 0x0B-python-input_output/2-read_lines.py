#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    c = 0
    c_ = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = file.readline()
            if line[-1:] == '\n':
                c += 1
            c += 1
    if nb_lines <= 0 or nb_lines >= c:
        with open(filename, encoding="utf-8") as file:
            print(file.read(), end="")
            return
    else:
        with open(filename, encoding="utf-8") as file:
            while nb_lines > c_:
                print(file.readline(), end="")
                c_ += 1
