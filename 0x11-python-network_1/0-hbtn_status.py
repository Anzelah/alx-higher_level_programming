#!/usr/bin/python3
"""Defines a module"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        page = res.read()
    print("Body response:")
    print("\t- type: {}" .format(type(page)))
    print("\t- content: {}" .format(page))
    print("\t- utf8 content: {}" .format(page.decode("utf-8")))
