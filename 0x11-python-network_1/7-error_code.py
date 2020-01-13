#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1])
    if r.raise_for_status():
        print(r.text):
    else:
        print("Error code: {}".format(r.status_code))
