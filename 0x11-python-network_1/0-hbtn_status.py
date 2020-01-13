#!/usr/bin/python3
""" urlib for first time check status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

        print("\t- type: {t}\n\t- content: {c}\n\t- utf8 content:{d}".format(
            t=type(html), c=html, d=html.decode('utf-8')))
