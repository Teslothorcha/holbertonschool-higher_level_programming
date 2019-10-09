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
    text = text.strip()
    l = len(text)
    id = 0
    while id in range(l):
        if text[id] == '?' or text[id] == ':' or text[id] == '.':
            if text[id] == '?':
                print('?')
            if text[id] == ':':
                print(':')
            if text[id] == '.':
                print('.')
            print()
            id += 1
            for idd in range(id, l):
                if text[idd] == ' ':
                    idd += 1
                    id = idd
                if text[idd] != ' ':
                    break
        print(text[id], end='')
        id += 1
