#!/usr/bin/python3
""" urlib for first time check status"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    content = r.text
    m2 = "- type: {t}".format(t=type(content))
    m3 = "- content: {c}".format(c=content)
    print("Body response:")
    print("\t{}\n\t{}".format(m2, m3))
