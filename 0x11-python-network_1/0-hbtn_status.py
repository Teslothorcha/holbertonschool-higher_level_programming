#!/usr/bin/python3
""" urlib for first time check status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

        m2="- type: {t}".format(t=type(html))
        m3="- content: {c}".format(c=html)
        m4="- utf8 content: {d}".format(d=html.decode('utf-8'))
        print("Body response:")
        print("\t{}\n\t{}\n\t{}".format(m2, m3, m4))
