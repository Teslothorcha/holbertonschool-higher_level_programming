#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    head = r.headers
    for var in head:
        if var == 'X-Request-Id':
            print(head[var])
