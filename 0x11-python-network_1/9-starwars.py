#!/usr/bin/python3
""" urlib for first time check status"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people', params={"search": argv[1]})
    j_s = r.json()
    print("Number of results: {}".format(j_s['count']))
    c = j_s['results']
    for l in c:
        print(l['name'])
