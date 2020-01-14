#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1]:
        var = argv[1]
    else:
        var = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = res.json()
        if not dic:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
    except ValueError:
        print("Not a valid JSON")