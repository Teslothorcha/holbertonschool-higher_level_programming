#!/usr/bin/python3
""" urlib for first time check header var"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info()["X-Request-Id"])
