#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    try:
        print(res.json()['id'])
    except KeyError:
        print("None")
