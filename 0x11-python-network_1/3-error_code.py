#!/usr/bin/python3
""" urlib for first POST request"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
            print("Error code: {error}".format(error=e.code))
