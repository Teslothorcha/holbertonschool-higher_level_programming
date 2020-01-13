#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    head = r.headers
    if 'X-Request-Id' in head:
        print(head['X-Request-Id'])
